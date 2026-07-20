from dataclasses import is_dataclass, fields, Field
from enum import Enum
from keyword import iskeyword, issoftkeyword
from typing import (
    TypedDict,
    Union,
    List,
    Literal,
    LiteralString,
    get_origin,
    get_args,
    get_type_hints,
    is_typeddict,
    Any,
)
from types import NoneType


def get_default_value(
    typ: type, *, only_required: bool = False, recursive: bool = False
) -> object:
    """Get 'type' default value

    * only_required: ignore field annotated with NotRequired
    * recursive: get value for field annotated with TypedDict class,
      if False(default) return 'MissingValue' object

    """
    return TypeDefaultGenerator(typ, only_required, recursive).get_default_value()


class TypeDefaultGenerator:
    """TypeValue default value generator"""

    def __init__(self, typ: type, only_required: bool = False):
        self.typ = typ
        self.only_required = only_required

    def get_default_value(self) -> object:
        """get default value"""
        return self._get_default_value(self.typ)

    def _get_typeddict(self, typ: TypedDict):
        type_hints = get_type_hints(typ)

        if self.only_required:
            keys = typ.__required_keys__
        else:
            keys = type_hints.keys()

        items = {}
        for key in keys:
            items[key] = (
                self._get_value_set(type_hints[key])
                if key == "valueSet"
                else self._get_default_value(type_hints[key])
            )

        return typ(items)

    def _get_dataclass(self, typ: type) -> object:
        type_hints = get_type_hints(typ)
        kwargs = {}
        for key in type_hints.keys():
            kwargs[key] = (
                self._get_value_set(type_hints[key])
                if key == "valueSet"
                else self._get_default_value(type_hints[key])
            )
        return typ(**kwargs)

    def _get_value_set(self, typ: List[Enum]) -> List[object]:
        origin = get_origin(typ)
        args = get_args(typ)
        items = args[0]
        if origin != list or not issubclass(items, Enum):
            raise ValueError("'valueSet' only accept list of Enum")
        return [i.value for i in items]

    def _get_default_value(self, typ: type) -> object:
        atomic_types = {int, float, str, bool}
        if typ in atomic_types:
            return typ()

        none_types = {
            None,  # e.g.: Union[str, None]
            type(None),  # e.g.: Optional[str]
        }
        if typ in none_types:
            return None

        origin = get_origin(typ)
        args = get_args(typ)

        if origin in {list, dict}:
            return origin()

        if origin == Union:
            # return first type
            return self._get_default_value(args[0])

        if origin in {Literal, LiteralString}:
            return args[0]

        if issubclass(typ, Enum):
            # return first enum
            return list(typ)[0]

        if is_typeddict(typ):
            return self._get_typeddict(typ)

        if is_dataclass(typ):
            return self._get_dataclass(typ)

        raise ValueError(f"unable get default value for {typ}")


# _ATOMIC_TYPE use tuple because isinstance() argument accept tuple
_ATOMIC_TYPE = (int, float, str, bool, NoneType)
_OPTIONAL_KEY = "optional"


def _is_keyword(name: str) -> bool:
    return iskeyword(name) or issoftkeyword(name)


def _is_optional_field(f: Field) -> bool:
    return f.metadata.get(_OPTIONAL_KEY, False)


def to_dict(obj: object) -> dict:
    """convert dataclass object to dict"""
    return ToDictConverter(obj).convert()


class ToDictConverter:
    def __init__(self, obj: object):
        self.obj = obj

    def convert(self) -> dict:
        return self._convert_object(self.obj)

    def _convert_object(self, obj: object) -> object:
        if isinstance(obj, Enum):
            return obj.value

        if isinstance(obj, _ATOMIC_TYPE):
            return obj

        if isinstance(obj, list):
            return [self._convert_object(o) for o in obj]

        if isinstance(obj, dict):
            return {k: self._convert_object(v) for k, v in obj.items()}

        if is_dataclass(obj):
            return self._convert_dataclass(obj)

        raise ValueError(f"unable convert {obj}")

    def _convert_field(self, parent: object, field: Field) -> tuple:
        name = field.name
        value = getattr(parent, name)
        if value is None:
            # omitted field
            if _is_optional_field(field):
                return None

        if _is_keyword(name[:-1]):
            # remove tail underscore, e.g: 'from_' -> 'from'
            name = name[:-1]

        value = self._convert_object(value)
        return name, value

    def _convert_dataclass(self, obj: object) -> dict:
        return dict([self._convert_field(obj, f) for f in fields(obj)])


def from_dict(dct: dict, typ: type) -> object:
    """convert dataclass object from dict"""
    return FromDictConverter(dct, typ).convert()


class FromDictConverter:
    def __init__(self, dct: dict, typ: type):
        self.dct = dct
        self.typ = typ

    def convert(self) -> object:
        return self._convert_object(self.dct, self.typ)

    def _convert_object(self, obj: Any, typ: type) -> object:
        origin = get_origin(typ)
        args = get_args(typ)

        if origin is list:
            return [self._convert_object(o, args[0]) for o in obj]

        if origin is dict:
            return {k: self._convert_object(v, args[1]) for k, v in obj.items()}

        if origin in {Literal, LiteralString}:
            return obj

        if origin is Union:
            # try to convert from all possible type
            for arg in args:
                try:
                    return self._convert_object(obj, arg)
                except Exception:
                    continue
            raise ValueError(f"unable convert {obj}")

        if is_dataclass(typ):
            return self._convert_dataclass(obj, typ)

        if is_typeddict(typ):
            return obj

        if issubclass(typ, Enum):
            return typ(obj)

        # Check atomic type after check enum because int defined in enum
        # is valid to isinstance of int
        if isinstance(obj, _ATOMIC_TYPE):
            return obj

        raise ValueError(f"unable convert {obj}")

    def _convert_field(self, dct: dict, field: Field, typ: type) -> dict:
        name = field.name
        value = dct.get(name, None)
        if value is None:
            # validate optional
            if not _is_optional_field(field):
                raise ValueError(f"{name} must assigned")

        value = self._convert_object(value, typ)
        return value

    def _convert_dataclass(self, dct: dict, typ: type) -> object:
        # Field.type sometimes return str instead the actual type
        type_hints = get_type_hints(typ)
        return typ(
            *[
                self._convert_field(dct, field, type_hints[field.name])
                for field in fields(typ)
            ]
        )

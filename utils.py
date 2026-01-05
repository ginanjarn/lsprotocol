from collections import ChainMap
from dataclasses import dataclass, is_dataclass, fields, Field
from enum import Enum
from functools import wraps
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
    Callable,
    Any,
)
from types import NoneType


def get_default_value(
    typ: type, *, only_required: bool = False, recursive: bool = False
) -> dict:
    """Get 'type' default value

    * only_required: ignore field annotated with NotRequired
    * recursive: get value for field annotated with TypedDict class,
      if False(default) return 'MissingValue' object

    """
    return TypeValue(typ, only_required, recursive).get_default()


class TypeValue:
    """TypeValue default value generator"""

    def __init__(self, typ: type, only_required: bool = False, recursive: bool = False):
        self.typ = typ
        self.only_required = only_required
        self.recursive = recursive

        self._enter_recursion = False

    def check_recursion(func: Callable[[...], Any]) -> Any:
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if self._enter_recursion and not self.recursive:
                try:
                    typ = args[0]
                except IndexError:
                    typ = kwargs["typ"]
                return RequiredValue(typ)

            self._enter_recursion = True
            ret = func(self, *args, **kwargs)
            self._enter_recursion = False
            return ret

        return wrapper

    def get_default(self) -> dict:
        """get default value"""
        return self._get_type_default(self.typ)

    @check_recursion
    def _get_typeddict_default(self, typ: TypedDict):
        data = {}
        type_hints = get_type_hints(typ)

        if self.only_required:
            keys = typ.__required_keys__
        else:
            keys = type_hints.keys()

        for key in keys:
            type_ = type_hints[key]
            if key == "valueSet":
                data[key] = self._get_valueset_default(type_)
            else:
                data[key] = self._get_type_default(type_)

        return data

    @check_recursion
    def _get_dataclass_default(self, typ: type) -> object:
        kwargs = {k: self._get_type_default(v) for k, v in get_type_hints(typ).items()}
        return typ(**kwargs)

    def _get_valueset_default(self, typ: List[Enum]) -> List[object]:
        origin = get_origin(typ)
        args = get_args(typ)
        items = args[0]
        if origin != list or not issubclass(items, Enum):
            raise ValueError("'valueSet' only accept list of Enum")
        return [i.value for i in items]

    def _get_type_default(self, typ: type) -> object:
        atomic_types = {
            int: 0,
            float: 0.0,
            str: "",
            bool: False,
            None: None,  # e.g.: Union[str,None]
            type(None): None,  # e.g.: Optional[str]
        }
        val = atomic_types.get(typ)
        if val is not None:
            return val

        origin = get_origin(typ)
        args = get_args(typ)

        if origin == list:
            return list()

        if origin == dict:
            return dict()

        if origin == Union:
            return self._get_type_default(args[0])

        if origin in {Literal, LiteralString}:
            return args[0]

        if issubclass(typ, Enum):
            return list(typ)[0].value

        if is_typeddict(typ):
            return self._get_typeddict_default(typ)

        if is_dataclass(typ):
            return self._get_dataclass_default(typ)

        raise ValueError(f"unable get default value for {typ}")


@dataclass
class RequiredValue:
    type_: type


_ATOMIC_TYPE = (int, float, str, bool, NoneType)


def _is_keyword(name: str) -> bool:
    return iskeyword(name) or issoftkeyword(name)


_OPTIONAL_KEY = "optional"


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
        if isinstance(obj, _ATOMIC_TYPE):
            return obj

        if isinstance(obj, list):
            return [self._convert_object(o) for o in obj]

        if isinstance(obj, dict):
            return {k: self._convert_object(v) for k, v in obj.items()}

        if isinstance(obj, Enum):
            return obj.value

        if is_dataclass(obj):
            return self._convert_dataclass(obj)

        raise ValueError(f"unable convert {obj}")

    def _field_to_data(self, obj: object, field: Field) -> dict:
        name = field.name
        value = getattr(obj, name)
        if value is None:
            # omitted field
            if _is_optional_field(field):
                return None

        if is_dataclass(field.type):
            value = self._convert_dataclass(value)

        if _is_keyword(name):
            # remove tail underscore, e.g: 'from_' -> 'from'
            name = name[:-1]

        return {name: value}

    def _convert_dataclass(self, obj: object) -> dict:
        data = [self._field_to_data(obj, f) for f in fields(obj)]
        return dict(ChainMap(*[d for d in data if d is not None]))


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
        if isinstance(obj, _ATOMIC_TYPE):
            return obj

        origin = get_origin(typ)
        args = get_args(typ)

        if origin is list:
            return [self._convert_object(o, args[0]) for o in obj]

        if origin is dict:
            return {k: self._convert_object(v, args[1]) for k, v in obj.items()}

        if origin is Union:
            for arg in args:
                try:
                    return self._convert_object(obj, arg)
                except Exception:
                    continue
            raise ValueError(f"unable convert {obj}")

        if origin in {Literal, LiteralString}:
            return obj

        if issubclass(typ, Enum):
            return typ(obj)

        if is_typeddict(typ):
            return obj

        if is_dataclass(typ):
            return self._convert_dataclass(obj, typ)

        raise ValueError(f"unable convert {obj}")

    def _field_to_kwarg(self, dct: dict, field: Field, type_hints: dict) -> dict:
        name = field.name
        typ = type_hints[name]
        value = dct.get(name, None)

        if value is None:
            # validate optional
            if not _is_optional_field(field):
                raise ValueError(f"{field.name} must assigned")

        else:
            # check dataclass if value is not None
            if is_dataclass(typ):
                value = self._convert_object(value, typ)

        if _is_keyword(name):
            # convert to valid identifier name, e.g.: 'from' -> 'from_'
            name = f"{name}_"

        return {name: value}

    def _convert_dataclass(self, dct: dict, typ: type) -> object:
        type_hints = get_type_hints(typ)
        kwargs = ChainMap(
            *[self._field_to_kwarg(dct, f, type_hints) for f in fields(typ)]
        )
        return typ(**kwargs)

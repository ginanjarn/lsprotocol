from dataclasses import is_dataclass
from enum import Enum
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
)


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

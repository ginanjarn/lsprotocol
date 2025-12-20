from dataclasses import dataclass
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
    typ: TypedDict, *, only_required: bool = False, recursive: bool = False
) -> dict:
    """Get TypedDict default value

    * only_required: ignore field annotated with NotRequired
    * recursive: get value for field annotated with TypedDict class,
      if False(default) return 'MissingValue' object

    """
    return TypedDictValue(typ, only_required, recursive).get_default()


class TypedDictValue:
    """TypedDict default value generator"""

    def __init__(
        self, typ: TypedDict, only_required: bool = False, recursive: bool = False
    ):
        self.typ = typ
        self.only_required = only_required
        self.recursive = recursive

    def get_default(self) -> dict:
        """get default value"""
        return self._get_typeddict_default(self.typ)

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

    def _get_valueset_default(self, typ: List[Enum]) -> List[object]:
        origin = get_origin(typ)
        args = get_args(typ)
        items = args[0]
        if origin != list or not isinstance(items, Enum):
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

        if is_typeddict(typ):
            if not self.recursive:
                return MissingValue(typ)
            return self._get_typeddict_default(typ)

        raise ValueError(f"unable get default value for {typ}")


@dataclass
class MissingValue:
    value: object

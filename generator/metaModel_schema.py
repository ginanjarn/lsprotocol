from enum import Enum
from dataclasses import dataclass
from typing import Literal, Union, Optional, List

# Type compatibility
URI = str
DocumentUri = str
integer = int
uinteger = int
decimal = float
RegExp = str
string = str
boolean = bool
null = None

number = Union[int, float]

Type = Union[
    "BaseType",
    "ReferenceType",
    "ArrayType",
    "MapType",
    "AndType",
    "OrType",
    "TupleType",
    "StructureLiteralType",
    "StringLiteralType",
    "IntegerLiteralType",
    "BooleanLiteralType",
]


class TypeKind(Enum):
    BASE = "base"
    REFERENCE = "reference"
    ARRAY = "array"
    MAP = "map"
    AND = "and"
    OR = "or"
    TUPLE = "tuple"
    LITERAL = "literal"
    STRINGLITERAL = "stringLiteral"
    INTEGERLITERAL = "integerLiteral"
    BOOLEANLITERAL = "booleanLiteral"


class BaseTypes(Enum):
    URI = "URI"
    DOCUMENTURI = "DocumentUri"
    INTEGER = "integer"
    UINTEGER = "uinteger"
    DECIMAL = "decimal"
    REGEXP = "RegExp"
    STRING = "string"
    BOOLEAN = "boolean"
    NULL = "null"


class MessageDirection(Enum):
    """
    Indicates in which direction a message is sent in the protocol.
    """

    CLIENTTOSERVER = "clientToServer"
    SERVERTOCLIENT = "serverToClient"
    BOTH = "both"


@dataclass
class BaseType:
    """
    Represents a base type like `string` or `DocumentUri`.
    """

    kind: Literal["base"]
    name: BaseTypes


@dataclass
class ReferenceType:
    """
    Represents a reference to another type (e.g. `TextDocument`).
    This is either a `Structure`, a `Enumeration` or a `TypeAlias`
    in the same meta model.
    """

    kind: Literal["reference"]
    name: string


@dataclass
class ArrayType:
    """
    Represents an array type (e.g. `List[TextDocument]`).
    """

    kind: Literal["array"]
    element: Type


class MapKeyTypeKind(str, Enum):
    URI = "URI"
    DocumentUri = "DocumentUri"
    string = "string"
    integer = "integer"


@dataclass
class MapKeyTypeOpt:
    """optional value of MapKeyType"""

    kind: Literal["base"]
    name: MapKeyTypeKind


MapKeyType = Union[MapKeyTypeOpt, ReferenceType]
"""
Represents a type that can be used as a key in a
map type. If a reference type is used then the
type must either resolve to a `string` or `integer`
type. (e.g. `type ChangeAnnotationIdentifier === string`).
"""


@dataclass
class MapType:
    """
    Represents a JSON object map
    (e.g. `interface Map<K extends string | integer, V> { [key: K] => V }`).
    """

    kind: Literal["map"]
    key: MapKeyType
    value: Type


@dataclass
class AndType:
    """
    Represents an `and`type
    (e.g. TextDocumentParams & WorkDoneProgressParams`).
    """

    kind: Literal["and"]
    items: List[Type]


@dataclass
class OrType:
    """
    Represents an `or` type
    (e.g. `Location | LocationLink`).
    """

    kind: Literal["or"]
    items: List[Type]


@dataclass
class TupleType:
    """
    Represents a `tuple` type
    (e.g. `[integer, integer]`).
    """

    kind: Literal["tuple"]
    items: List[Type]


@dataclass
class Property:
    """
    Represents an object property.
    """

    name: string
    """
     The property name
    """

    type: Type
    """
     The type of the property
    """

    optional: Optional[boolean]
    """
     Whether the property is optional. If
     omitted, the property is mandatory.
    """

    documentation: Optional[string]
    """
     An optional documentation.
    """

    since: Optional[string]
    """
     Since when (release number) this property is
     available. Is undefined if not known.
    """

    sinceTags: Optional[List[string]]
    """
     All since tags in case there was more than one tag.
     Is undefined if not known.
    """

    proposed: Optional[boolean]
    """
     Whether this is a proposed property. If omitted,
     the structure is final.
    """

    deprecated: Optional[string]
    """
     Whether the property is deprecated or not. If deprecated
     the property contains the deprecation message.
    """


@dataclass
class StructureLiteral:
    """
    Defines an unnamed structure of an object literal.
    """

    properties: List[Property]
    """
     The properties.
    """

    documentation: Optional[string]
    """
     An optional documentation.
    """

    since: Optional[string]
    """
     Since when (release number) this structure is
     available. Is undefined if not known.
    """

    sinceTags: Optional[List[string]]
    """
     All since tags in case there was more than one tag.
     Is undefined if not known.
    """

    proposed: Optional[boolean]
    """
     Whether this is a proposed structure. If omitted,
     the structure is final.
    """

    deprecated: Optional[string]
    """
     Whether the literal is deprecated or not. If deprecated
     the property contains the deprecation message.
    """


@dataclass
class StructureLiteralType:
    """
    Represents a literal structure
    (e.g. `property: { start: uinteger end: uinteger }`).
    """

    kind: Literal["literal"]
    value: StructureLiteral


@dataclass
class StringLiteralType:
    """
    Represents a string literal type
    (e.g. `kind: Literal['rename']`).
    """

    kind: Literal["stringLiteral"]
    value: string


@dataclass
class IntegerLiteralType:
    """
    Represents an integer literal type
    (e.g. `kind: 1`).
    """

    kind: Literal["integerLiteral"]
    value: number


@dataclass
class BooleanLiteralType:
    """
    Represents a boolean literal type
    (e.g. `kind: true`).
    """

    kind: Literal["booleanLiteral"]
    value: boolean


@dataclass
class Request:
    """
    Represents a LSP request
    """

    method: string
    """
	 The request's method name.
	"""

    typeName: Optional[string]
    """
	 The type name of the request if any.
	"""

    params: Optional[Union[Type, List[Type]]]
    """
	 The parameter type(s) if any.
	"""

    result: Type
    """
	 The result type.
	"""

    partialResult: Optional[Type]
    """
	 Optional partial result type if the request
	 supports partial result reporting.
	"""

    errorData: Optional[Type]
    """
	 An optional error data type.
	"""

    registrationMethod: Optional[string]
    """
	 Optional a dynamic registration method if it
	 different from the request's method.
	"""

    registrationOptions: Optional[Type]
    """
	 Optional registration options if the request
	 supports dynamic registration.
	"""

    messageDirection: MessageDirection
    """
	 The direction in which this request is sent
	 in the protocol.
	"""

    documentation: Optional[string]
    """
	 An optional documentation
	"""

    since: Optional[string]
    """
	 Since when (release number) this request is
	 available. Is undefined if not known.
	"""

    sinceTags: Optional[List[string]]
    """
	 All since tags in case there was more than one tag.
	 Is undefined if not known.
	"""

    proposed: Optional[boolean]
    """
	 Whether this is a proposed feature. If omitted
	 the feature is final.
	"""

    deprecated: Optional[string]
    """
	 Whether the request is deprecated or not. If deprecated
	 the property contains the deprecation message.
	"""


@dataclass
class Notification:
    """
    Represents a LSP notification
    """

    method: string
    """
	 The notifications's method name.
	"""

    typeName: Optional[string]
    """
	 The type name of the notifications if any.
	"""

    params: Optional[Union[Type, List[Type]]]
    """
	 The parameter type(s) if any.
	"""

    registrationMethod: Optional[string]
    """
	 Optional a dynamic registration method if it
	 different from the notifications's method.
	"""

    registrationOptions: Optional[Type]
    """
	 Optional registration options if the notification
	 supports dynamic registration.
	"""

    messageDirection: MessageDirection
    """
	 The direction in which this notification is sent
	 in the protocol.
	"""

    documentation: Optional[string]
    """
	 An optional documentation
	"""

    since: Optional[string]
    """
	 Since when (release number) this notification is
	 available. Is undefined if not known.
	"""

    sinceTags: Optional[List[string]]
    """
	 All since tags in case there was more than one tag.
	 Is undefined if not known.
	"""

    proposed: Optional[boolean]
    """
	 Whether this is a proposed notification. If omitted
	 the notification is final.
	"""

    deprecated: Optional[string]
    """
	 Whether the notification is deprecated or not. If deprecated
	 the property contains the deprecation message.
	"""


@dataclass
class Structure:
    """
    Defines the structure of an object literal.
    """

    name: string
    """
	 The name of the structure.
	"""

    extends: Optional[List[Type]]
    """
	 Structures extended from. This structures form
	 a polymorphic type hierarchy.
	"""

    mixins: Optional[List[Type]]
    """
	 Structures to mix in. The properties of these
	 structures are `copied` into this structure.
	 Mixins don't form a polymorphic type hierarchy in
	 LSP.
	"""

    properties: List[Property]
    """
	 The properties.
	"""

    documentation: Optional[string]
    """
	 An optional documentation
	"""

    since: Optional[string]
    """
	 Since when (release number) this structure is
	 available. Is undefined if not known.
	"""

    sinceTags: Optional[List[string]]
    """
	 All since tags in case there was more than one tag.
	 Is undefined if not known.
	"""

    proposed: Optional[boolean]
    """
	 Whether this is a proposed structure. If omitted,
	 the structure is final.
	"""

    deprecated: Optional[string]
    """
	 Whether the structure is deprecated or not. If deprecated
	 the property contains the deprecation message.
	"""


@dataclass
class TypeAlias:
    """
    Defines a type alias.
    (e.g. `type Definition = Location | LocationLink`)
    """

    name: string
    """
	 The name of the type alias.
	"""

    type: Type
    """
	 The aliased type.
	"""

    documentation: Optional[string]
    """
	 An optional documentation.
	"""

    since: Optional[string]
    """
	 Since when (release number) this structure is
	 available. Is undefined if not known.
	"""

    sinceTags: Optional[List[string]]
    """
	 All since tags in case there was more than one tag.
	 Is undefined if not known.
	"""

    proposed: Optional[boolean]
    """
	 Whether this is a proposed type alias. If omitted,
	 the type alias is final.
	"""

    deprecated: Optional[string]
    """
	 Whether the type alias is deprecated or not. If deprecated
	 the property contains the deprecation message.
	"""


@dataclass
class EnumerationEntry:
    """
    Defines an enumeration entry.
    """

    name: string
    """
	 The name of the enum item.
	"""

    value: Union[string, number]
    """
	 The value.
	"""

    documentation: Optional[string]
    """
	 An optional documentation.
	"""

    since: Optional[string]
    """
	 Since when (release number) this enumeration entry is
	 available. Is undefined if not known.
	"""

    sinceTags: Optional[List[string]]
    """
	 All since tags in case there was more than one tag.
	 Is undefined if not known.
	"""

    proposed: Optional[boolean]
    """
	 Whether this is a proposed enumeration entry. If omitted,
	 the enumeration entry is final.
	"""

    deprecated: Optional[string]
    """
	 Whether the enum entry is deprecated or not. If deprecated
	 the property contains the deprecation message.
	"""


class EnumerationTypeName(Enum):
    STRING = "string"
    INTEGER = "integer"
    UINTEGER = "uinteger"


@dataclass
class EnumerationType:
    kind: Literal["base"]
    name: EnumerationTypeName


@dataclass
class Enumeration:
    """
    Defines an enumeration.
    """

    name: string
    """
	 The name of the enumeration.
	"""

    type: EnumerationType
    """
	 The type of the elements.
	"""

    values: List[EnumerationEntry]
    """
	 The enum values.
	"""

    supportsCustomValues: Optional[boolean]
    """
	 Whether the enumeration supports custom values (e.g. values which are not
	 part of the set defined in `values`). If omitted no custom values are
	 supported.
	"""

    documentation: Optional[string]
    """
	 An optional documentation.
	"""

    since: Optional[string]
    """
	 Since when (release number) this enumeration is
	 available. Is undefined if not known.
	"""

    sinceTags: Optional[List[string]]
    """
	 All since tags in case there was more than one tag.
	 Is undefined if not known.
	"""

    proposed: Optional[boolean]
    """
	 Whether this is a proposed enumeration. If omitted,
	 the enumeration is final.
	"""

    deprecated: Optional[string]
    """
	 Whether the enumeration is deprecated or not. If deprecated
	 the property contains the deprecation message.
	"""


@dataclass
class MetaData:
    """
    The protocol version.
    """

    version: string


@dataclass
class MetaModel:
    """
    The actual meta model.
    """

    metaData: MetaData
    """
	 Additional meta data.
	"""

    requests: List[Request]
    """
	 The requests.
	"""

    notifications: List[Notification]
    """
	 The notifications.
	"""

    structures: List[Structure]
    """
	 The structures.
	"""

    enumerations: List[Enumeration]
    """
	 The enumerations.
	"""

    typeAliases: List[TypeAlias]
    """
	 The type aliases.
	"""

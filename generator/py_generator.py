import re
from collections import OrderedDict
from dataclasses import dataclass
from keyword import iskeyword, issoftkeyword
from textwrap import indent as indent_text
from typing import List, Optional, Union


from metaModel_schema import (
    MetaModel,
    Type,
    BaseType,
    ReferenceType,
    ArrayType,
    MapType,
    AndType,
    OrType,
    TupleType,
    StructureLiteralType,
    StringLiteralType,
    IntegerLiteralType,
    BooleanLiteralType,
    MessageDirection,
    Request,
    Notification,
    Property,
    Structure,
    StructureLiteral,
    EnumerationType,
    Enumeration,
    TypeAlias,
    MetaData,
)


def make_docstring(text: str) -> str:
    escaped_text = (
        text.replace("\\r", "\\\\r").replace("\\n", "\\\\n").replace("\\t", "\\\\t")
    )
    if "\\" in escaped_text:
        return f'r"""{escaped_text}"""'
    return f'"""{escaped_text}"""'


def to_snake_case(text: str) -> str:
    return re.sub(r"([^A-Z])([A-Z])", r"\1_\2", text).lower()


@dataclass
class Imports:
    names: Union[List[str], str]

    def __post_init__(self):
        if isinstance(self.names, str):
            self.names = [self.names]

    def get_code(self) -> str:
        names = ", ".join(self.names)
        return f"import {names}"


@dataclass
class FromImports:
    module: str
    names: Union[List[str], str]

    def __post_init__(self):
        if isinstance(self.names, str):
            self.names = [self.names]

    def get_code(self) -> str:
        if len(self.names) > 3:
            names = ",\n\t".join(self.names)
            return f"from {self.module} import (\n\t{names}\n)"
        else:
            names = ", ".join(self.names)
            return f"from {self.module} import {names}"


@dataclass
class Variable:
    name: str
    annotation: Optional[str] = None
    value: Optional[str] = None
    docstring: Optional[str] = None

    def __post_init__(self):
        if all([self.annotation is None, self.value is None]):
            raise ValueError("annotation or value must assigned")

    def get_code(self) -> str:
        var_name = self.name
        if iskeyword(var_name) or issoftkeyword(var_name):
            var_name = f"{var_name}_"

        code = [var_name]
        if self.annotation:
            code.append(f": {self.annotation}")
        if self.value is not None:
            code.append(f" = {self.value}")
        if self.docstring:
            code.append("\n" + make_docstring(self.docstring))
        return "".join(code)


@dataclass
class Argument:
    name: str
    annotation: Optional[str] = None
    value: Optional[str] = None

    def get_code(self):
        code = [self.name]
        if self.annotation:
            code.append(f": {self.annotation}")
        if self.value:
            code.append(f"={self.value}")
        return "".join(code)


@dataclass
class Function:
    name: str
    arguments: Optional[List[Argument]] = None
    annotation: Optional[str] = None
    body: Optional[str] = None
    decorators: Optional[List[str]] = None
    docstring: Optional[str] = None

    def get_code(self):
        code = ["def ", self.name, "("]
        if self.decorators:
            code.insert(0, "\n".join(self.decorators) + "\n")

        if self.arguments:
            arguments = ", ".join([arg.get_code() for arg in self.arguments])
            code.append(arguments)
        code.append(")")

        if self.annotation:
            code.append(f" -> {self.annotation}")
        code.append(":\n")

        func_body = []
        if self.docstring:
            func_body.append(make_docstring(self.docstring))
        if self.body:
            func_body.append(self.body)

        if not func_body:
            func_body.append(make_docstring(""))

        body_code = "\n".join(func_body)
        code.append(indent_text(body_code, "\t"))

        return "".join(code)


@dataclass
class Class:
    name: str
    variables: Optional[List[Variable]] = None
    methods: Optional[List[Function]] = None
    parents: Optional[List[str]] = None
    decorators: Optional[List[str]] = None
    docstring: Optional[str] = None

    def get_code(self):
        code = ["class ", self.name]
        if self.decorators:
            code.insert(0, "\n".join(self.decorators) + "\n")
        if self.parents:
            parents = ", ".join([parent for parent in self.parents])
            code.append(f"({parents})")
        code.append(":\n")

        class_body = []
        if self.docstring:
            class_body.append(make_docstring(self.docstring))

        if self.variables:

            def quote(var: Variable) -> Variable:
                if var.annotation is None:
                    annotation = var.annotation
                else:
                    annotation = re.sub(rf"\b({self.name})\b", r'"\1"', var.annotation)
                return Variable(var.name, annotation, var.value, var.docstring)

            quoted_variable = [quote(var) for var in self.variables]
            variable = "\n".join([var.get_code() for var in quoted_variable])
            class_body.append(variable + "\n")
        if self.methods:
            method = "\n\n".join([method.get_code() for method in self.methods])
            class_body.append(method + "\n")

        if not class_body:
            class_body.append(make_docstring(""))

        class_body_code = "\n".join(class_body)
        code.append(indent_text(class_body_code, "\t"))

        return "".join(code)


class CodeGenerator:
    def __init__(self, model: MetaModel) -> None:
        self.model = model

        self._types = []
        self._server = Class("Server", methods=list(), variables=list())
        self._server_handle_map = {}
        self._client = Class("Client", methods=list(), variables=list())
        self._client_handle_map = {}

        self._structure_maps = {i.name: i for i in model.structures}

        self._is_generated = False

    def generate(self) -> None:

        self.metadata(self.model.metaData)

        for enumeration in self.model.enumerations:
            code = self.type_(enumeration)
            self._types.append(code)

        for structure in self.model.structures:
            code = self.type_(structure)
            self._types.append(code)

        for typealias in self.model.typeAliases:
            code = self.type_(typealias)
            self._types.append(code)

        for request in self.model.requests:
            self.request(request)

        for notification in self.model.notifications:
            self.notification(notification)

        self._is_generated = True

    @property
    def types_code(self) -> str:
        if not self._is_generated:
            raise Exception("code not generated yet")

        imports = [
            FromImports("__future__", ["annotations"]),
            FromImports("enum", ["Enum"]),
            FromImports(
                "typing",
                [
                    "List",
                    "Dict",
                    "Union",
                    "Tuple",
                    "Literal",
                    "TypeAlias",
                    "TypedDict",
                    "NotRequired",
                ],
            ),
        ]

        base_aliases = [
            Variable("uinteger", "TypeAlias", "int"),
            Variable("URI", "TypeAlias", "str"),
            Variable("DocumentUri", "TypeAlias", "str"),
            Variable("RegExp", "TypeAlias", "str"),
        ]
        self._types = base_aliases + self._types

        ordered_types = NameOrderer(self._types).ordered_names()
        types = imports + ordered_types

        types_code = [t.get_code() for t in types]
        return "\n\n".join(types_code)

    @property
    def server_code(self) -> str:
        if not self._is_generated:
            raise Exception("code not generated yet")

        handle_map = ",\n\t".join(
            [f"{k!r}: self.{v}" for k, v in self._server_handle_map.items()]
        )
        body = (
            f"handle_map = {{\n\t{handle_map}\n\t}}\n"
            "return handle_map[method](params_or_result)\n"
        )
        self._server.methods.append(
            Function(
                "handle",
                arguments=[
                    Argument("self"),
                    Argument("method", "str"),
                    Argument("params_or_result", "LSPAny"),
                ],
                annotation="None",
                body=body,
            ),
        )
        protocol_imports = ImportsManager([self._server], self._types).resolve()
        imports = [
            FromImports("typing", ["List", "Union"]),
            FromImports(".lsprotocol", protocol_imports),
        ]
        server_types = imports + [self._server]

        return "\n\n".join([c.get_code() for c in server_types])

    @property
    def client_code(self) -> str:
        if not self._is_generated:
            raise Exception("code not generated yet")

        handle_map = ",\n\t".join(
            [f"{k!r}: self.{v}" for k, v in self._client_handle_map.items()]
        )
        body = (
            f"handle_map = {{\n\t{handle_map}\n\t}}\n"
            "return handle_map[method](params_or_result)\n"
        )
        self._client.methods.append(
            Function(
                "handle",
                arguments=[
                    Argument("self"),
                    Argument("method", "str"),
                    Argument("params_or_result", "LSPAny"),
                ],
                annotation="None",
                body=body,
            ),
        )

        protocol_imports = ImportsManager([self._client], self._types).resolve()
        imports = [
            FromImports("typing", ["List", "Union"]),
            FromImports(".lsprotocol", protocol_imports),
        ]
        client_code = "\n\n".join([c.get_code() for c in imports + [self._client]])
        return client_code

    def type_(self, tp: Type) -> str:
        if tp is None:
            return "None"

        type_map = {
            "base": self.basetype,
            "reference": self.referencetype,
            "array": self.arraytype,
            "map": self.maptype,
            "and": self.andtype,
            "or": self.ortype,
            "tuple": self.tupletype,
            "literal": self.literaltype,
            "stringLiteral": self.stringliteraltype,
            "integerLiteral": self.integerliteraltype,
            "booleanLiteral": self.booleanliteraltype,
        }

        try:
            fn = type_map[tp.kind]
        except (KeyError, AttributeError):
            method = type(tp).__name__.lower()
            fn = getattr(self, method)

        try:
            code = fn(tp)
            return code
        except Exception as err:
            raise err

    def basetype(self, tp: BaseType) -> str:
        builtin_type_map = {
            "integer": "int",
            "decimal": "float",
            "string": "str",
            "boolean": "bool",
            "null": "None",
        }
        tp_name = tp.name.value
        if builtin_type := builtin_type_map.get(tp_name):
            return builtin_type
        return tp_name

    def referencetype(self, tp: ReferenceType) -> str:
        return f"{tp.name}"

    def arraytype(self, tp: ArrayType) -> str:
        code = self.type_(tp.element)
        return f"List[{code}]"

    def maptype(self, tp: MapType) -> str:
        key = self.type_(tp.key)
        value = self.type_(tp.value)
        return f"Dict[{key}, {value}]"

    def andtype(self, tp: AndType) -> str:
        code = ", ".join([self.type_(c) for c in tp.items])
        return f"Union[{code}]"

    def ortype(self, tp: OrType) -> str:
        code = ", ".join([self.type_(c) for c in tp.items])
        return f"Union[{code}]"

    def tupletype(self, tp: TupleType) -> str:
        code = ", ".join([self.type_(c) for c in tp.items])
        return f"Tuple[{code}]"

    def literaltype(self, tp: StructureLiteralType) -> str:
        return f"Literal[{self.type_(tp.value)!r}]"

    def stringliteraltype(self, tp: StringLiteralType) -> str:
        return f"Literal[{tp.value!r}]"

    def integerliteraltype(self, tp: IntegerLiteralType) -> str:
        return f"Literal[{tp.value!r}]"

    def booleanliteraltype(self, tp: BooleanLiteralType) -> str:
        return f"Literal[{tp.value!r}]"

    def metadata(self, tp: MetaData) -> None:
        pass

    def request(self, tp: Request) -> None:
        func_name = to_snake_case(tp.typeName)
        handle_func_name = "handle_" + func_name
        request_function = Function(
            func_name,
            arguments=[
                Argument("self"),
                Argument("params", self.type_(tp.params)),
            ],
            annotation="None",
            body=f"self.request(method={tp.method!r}, params=params)",
            docstring=tp.documentation,
        )
        handle_result_function = Function(
            handle_func_name,
            arguments=[
                Argument("self"),
                Argument("context", "dict"),
                Argument("result", self.type_(tp.result)),
            ],
            annotation="None",
        )
        handle_request_function = Function(
            handle_func_name,
            arguments=[
                Argument("self"),
                Argument("context", "dict"),
                Argument("params", self.type_(tp.params)),
            ],
            annotation=self.type_(tp.result),
        )
        if tp.messageDirection in {
            MessageDirection.CLIENTTOSERVER,
            MessageDirection.BOTH,
        }:
            self._client.methods.append(request_function)
            self._client.methods.append(handle_result_function)
            self._client_handle_map[tp.method] = handle_func_name

            self._server.methods.append(handle_request_function)
            self._server_handle_map[tp.method] = handle_func_name

        if tp.messageDirection in {
            MessageDirection.SERVERTOCLIENT,
            MessageDirection.BOTH,
        }:
            self._server.methods.append(request_function)
            self._server.methods.append(handle_result_function)
            self._server_handle_map[tp.method] = handle_func_name

            self._client.methods.append(handle_request_function)
            self._client_handle_map[tp.method] = handle_func_name

    def notification(self, tp: Notification) -> None:
        func_name = to_snake_case(tp.typeName)
        handle_func_name = "handle_" + func_name
        notify_function = Function(
            func_name,
            arguments=[
                Argument("self"),
                Argument("params", self.type_(tp.params)),
            ],
            annotation="None",
            body=f"self.notify(method={tp.method!r}, params=params)",
            docstring=tp.documentation,
        )
        handle_notification_function = Function(
            handle_func_name,
            arguments=[
                Argument("self"),
                Argument("context", "dict"),
                Argument("params", self.type_(tp.params)),
            ],
            annotation="None",
        )
        if tp.messageDirection in {
            MessageDirection.CLIENTTOSERVER,
            MessageDirection.BOTH,
        }:
            self._client.methods.append(notify_function)

            self._server.methods.append(handle_notification_function)
            self._server_handle_map[tp.method] = handle_func_name

        if tp.messageDirection in {
            MessageDirection.SERVERTOCLIENT,
            MessageDirection.BOTH,
        }:
            self._server.methods.append(notify_function)

            self._client.methods.append(handle_notification_function)
            self._client_handle_map[tp.method] = handle_func_name

    def property(self, tp: Property) -> Variable:
        type_ = self.type_(tp.type)
        if tp.optional:
            type_ = f"NotRequired[{type_}]"
        return Variable(tp.name, type_, docstring=tp.documentation)

    def pull_reference(self, tp: ReferenceType) -> Structure:
        return self._structure_maps[tp.name]

    def structure(self, tp: Structure) -> str:
        parents = []
        if tp.extends:
            parents += [self.type_(p) for p in tp.extends]
        else:
            parents += ["TypedDict"]

        properties = tp.properties or list()
        if tp.mixins:
            for mixin in tp.mixins:
                ref = self.pull_reference(mixin)
                properties.extend(ref.properties)

        variables = [self.property(p) for p in properties]
        return Class(
            tp.name,
            parents=parents,
            variables=variables,
            docstring=tp.documentation,
        )

    def structureliteral(self, tp: StructureLiteral) -> str:
        return "\n".join([self.property(p) for p in tp.properties])

    def enumerationtype(self, tp: EnumerationType) -> str:
        return tp.name.value

    def enumeration(self, tp: Enumeration) -> str:
        entries = [Variable(val.name, value=f"{val.value!r}") for val in tp.values]
        return Class(tp.name, parents=[self.type_(tp.type), "Enum"], variables=entries)

    def typealias(self, tp: TypeAlias) -> str:
        typ = self.type_(tp.type)
        typ = re.sub(r"\b(LSPObject|LSPArray)\b", r'"\1"', typ)
        return Variable(
            tp.name, annotation="TypeAlias", value=typ, docstring=tp.documentation
        )


class NameOrderer:
    """Name Orderer

    Order name by depedencies, make required class (for example base class)
    above consumer class.
    """

    def __init__(self, names: List[Union[Class, Variable]]):
        self.names = names
        self.name_map = {tp.name: tp for tp in names}
        self.ordered_name_map = OrderedDict()

        self.defined_names = []

    def ordered_names(self) -> List[Union[Class, Variable]]:
        """return ordered names"""
        for name in self.names:
            self.define_name(name)

        ordered = []
        defined = set()
        for name in self.defined_names:
            if name in defined:
                continue

            defined.add(name)
            ordered.append(self.name_map[name])

        return ordered

    def define_name(self, name: Union[Class, Variable]) -> None:
        identifier_pattern = re.compile(r"([a-zA-Z_]\w+)")

        if isinstance(name, Class):
            for parent in name.parents:
                if parent in self.defined_names:
                    continue
                if parent_obj := self.name_map.get(parent):
                    self.define_name(parent_obj)

            for var in name.variables:
                if annotation := var.annotation:
                    for typ in identifier_pattern.findall(annotation):
                        if typ in self.defined_names:
                            continue
                        if typ_obj := self.name_map.get(typ):
                            try:
                                self.define_name(typ_obj)
                            except RecursionError:
                                pass

            self.defined_names.append(name.name)

        if isinstance(name, Variable):
            name: Variable

            if name.annotation == "TypeAlias":
                for typ in identifier_pattern.findall(name.value):
                    if typ in self.defined_names:
                        continue
                    if typ_obj := self.name_map.get(typ):
                        try:
                            self.define_name(typ_obj)
                        except RecursionError:
                            pass

            self.defined_names.append(name.name)


class ImportsManager:

    def __init__(
        self,
        consumer_names: List[Union[Class, Variable]],
        defined_names: List[Union[Class, Variable]],
    ):
        self.consumer_names = consumer_names
        self.defined_names = defined_names

    def resolve(self) -> List[str]:
        """resolve imports"""

        identifier_pattern = re.compile(r"([a-zA-Z_]\w+)")

        names = set([name.name for name in self.defined_names])

        imports = []

        for name in self.consumer_names:
            if isinstance(name, Class):
                name: Class
                if name.parents:
                    for parent in name.parents:
                        if parent in imports:
                            continue
                        if parent in names:
                            imports.append(parent)

                if name.variables:
                    for var in name.variables:
                        if annotation := var.annotation:
                            for typ in identifier_pattern.findall(annotation):
                                if typ in imports:
                                    continue
                                if typ in names:
                                    imports.append(typ)
                if name.methods:
                    for func in name.methods:
                        for arg in func.arguments:
                            if annotation := arg.annotation:
                                for typ in identifier_pattern.findall(annotation):
                                    if typ in imports:
                                        continue
                                    if typ in names:
                                        imports.append(typ)

                        if annotation := func.annotation:
                            for typ in identifier_pattern.findall(annotation):
                                if typ in imports:
                                    continue
                                if typ in names:
                                    imports.append(typ)

            if isinstance(name, Variable):
                name: Variable

                if annotation := name.annotation:
                    for typ in identifier_pattern.findall(annotation):
                        if typ in imports:
                            continue
                        if typ in names:
                            imports.append(typ)

                if name.annotation == "TypeAlias":
                    for typ in identifier_pattern.findall(name.value):
                        if typ in imports:
                            continue
                        if typ in names:
                            imports.append(typ)

        return imports

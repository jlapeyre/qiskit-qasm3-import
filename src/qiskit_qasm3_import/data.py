import enum
from typing import Any, Optional
from openqasm3 import ast

from . import types


class Scope(enum.Enum):
    """Types of scope in OpenQASM 3 programs."""

    GLOBAL = enum.auto()
    GATE = enum.auto()
    FUNCTION = enum.auto()
    LOCAL = enum.auto()
    CALIBRATION = enum.auto()
    BUILTIN = enum.auto()
    # NONE scope is for when we're adding an implicit symbol to the table, but it shouldn't actually
    # be accessible by anything outside the context that defines it.  We might need to do this in
    # order to reserve a name that's being defined in the output circuit, but isn't present in the
    # OQ3 program.
    NONE = enum.auto()


class AddressingMode(enum.Enum):
    """Addressing mode for qubits in OpenQASM 3 programs.

    This class is useful as long as we allow only physical or virtual addressing modes, but
    not mixed. If the latter is supported in the future, this class will be modified or removed.
    """

    UNKNOWN = enum.auto()
    PHYSICAL = enum.auto()
    VIRTUAL = enum.auto()


class Symbol:
    """An internal symbol used during parsing."""

    __slots__ = ("name", "data", "type", "scope", "definer")

    def __init__(
        self,
        name: str,
        data: Any,
        type: types.Type,
        scope: Scope,
        definer: Optional[ast.QASMNode] = None,
    ):
        self.name = name
        self.data = data
        self.type = type
        self.scope = scope
        self.definer = definer

from typing import NamedTuple, Any

class Pair(NamedTuple):
    key: Any
    value: Any

DELETED = object()
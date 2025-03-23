from ..imports import types
from abc import abstractmethod
from typing import List, Protocol, Tuple

Descriptor = types.Descriptor
class HostPreopens(Protocol):
    @abstractmethod
    def get_directories(self) -> List[Tuple[Descriptor, str]]:
        raise NotImplementedError


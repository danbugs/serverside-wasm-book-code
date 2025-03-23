from ..types import Result
from abc import abstractmethod
from typing import Protocol

class HostExit(Protocol):
    @abstractmethod
    def exit(self, status: Result[None, None]) -> None:
        raise NotImplementedError


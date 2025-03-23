from ..imports import streams
from abc import abstractmethod
from typing import Protocol

InputStream = streams.InputStream
class HostStdin(Protocol):
    @abstractmethod
    def get_stdin(self) -> InputStream:
        raise NotImplementedError


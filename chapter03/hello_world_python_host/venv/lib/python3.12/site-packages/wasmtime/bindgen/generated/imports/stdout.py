from ..imports import streams
from abc import abstractmethod
from typing import Protocol

OutputStream = streams.OutputStream
class HostStdout(Protocol):
    @abstractmethod
    def get_stdout(self) -> OutputStream:
        raise NotImplementedError


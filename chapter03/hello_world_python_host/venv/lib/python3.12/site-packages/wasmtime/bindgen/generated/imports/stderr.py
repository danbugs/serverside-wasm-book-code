from ..imports import streams
from abc import abstractmethod
from typing import Protocol

OutputStream = streams.OutputStream
class HostStderr(Protocol):
    @abstractmethod
    def get_stderr(self) -> OutputStream:
        raise NotImplementedError


from ..types import Result
from abc import abstractmethod
from enum import Enum
from typing import Protocol, Tuple

InputStream = int
OutputStream = int
class StreamStatus(Enum):
    OPEN = 0
    ENDED = 1

class HostStreams(Protocol):
    @abstractmethod
    def drop_input_stream(self, this: InputStream) -> None:
        raise NotImplementedError
    @abstractmethod
    def write(self, this: OutputStream, buf: bytes) -> Result[Tuple[int, StreamStatus], None]:
        raise NotImplementedError
    @abstractmethod
    def blocking_write(self, this: OutputStream, buf: bytes) -> Result[Tuple[int, StreamStatus], None]:
        raise NotImplementedError
    @abstractmethod
    def drop_output_stream(self, this: OutputStream) -> None:
        raise NotImplementedError


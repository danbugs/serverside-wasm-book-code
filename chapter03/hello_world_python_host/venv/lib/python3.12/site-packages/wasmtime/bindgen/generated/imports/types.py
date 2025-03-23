from ..imports import streams
from ..types import Result
from abc import abstractmethod
from enum import Enum
from typing import Protocol

Descriptor = int
Filesize = int
OutputStream = streams.OutputStream
class ErrorCode(Enum):
    ACCESS = 0
    WOULD_BLOCK = 1
    ALREADY = 2
    BAD_DESCRIPTOR = 3
    BUSY = 4
    DEADLOCK = 5
    QUOTA = 6
    EXIST = 7
    FILE_TOO_LARGE = 8
    ILLEGAL_BYTE_SEQUENCE = 9
    IN_PROGRESS = 10
    INTERRUPTED = 11
    INVALID = 12
    IO = 13
    IS_DIRECTORY = 14
    LOOP = 15
    TOO_MANY_LINKS = 16
    MESSAGE_SIZE = 17
    NAME_TOO_LONG = 18
    NO_DEVICE = 19
    NO_ENTRY = 20
    NO_LOCK = 21
    INSUFFICIENT_MEMORY = 22
    INSUFFICIENT_SPACE = 23
    NOT_DIRECTORY = 24
    NOT_EMPTY = 25
    NOT_RECOVERABLE = 26
    UNSUPPORTED = 27
    NO_TTY = 28
    NO_SUCH_DEVICE = 29
    OVERFLOW = 30
    NOT_PERMITTED = 31
    PIPE = 32
    READ_ONLY = 33
    INVALID_SEEK = 34
    TEXT_FILE_BUSY = 35
    CROSS_DEVICE = 36

class DescriptorType(Enum):
    UNKNOWN = 0
    BLOCK_DEVICE = 1
    CHARACTER_DEVICE = 2
    DIRECTORY = 3
    FIFO = 4
    SYMBOLIC_LINK = 5
    REGULAR_FILE = 6
    SOCKET = 7

class HostTypes(Protocol):
    @abstractmethod
    def write_via_stream(self, this: Descriptor, offset: Filesize) -> Result[OutputStream, ErrorCode]:
        raise NotImplementedError
    @abstractmethod
    def append_via_stream(self, this: Descriptor) -> Result[OutputStream, ErrorCode]:
        raise NotImplementedError
    @abstractmethod
    def get_type(self, this: Descriptor) -> Result[DescriptorType, ErrorCode]:
        raise NotImplementedError
    @abstractmethod
    def drop_descriptor(self, this: Descriptor) -> None:
        raise NotImplementedError


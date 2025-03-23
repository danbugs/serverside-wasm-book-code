from abc import abstractmethod
from typing import Protocol

class HostRandom(Protocol):
    @abstractmethod
    def get_random_bytes(self, len: int) -> bytes:
        raise NotImplementedError


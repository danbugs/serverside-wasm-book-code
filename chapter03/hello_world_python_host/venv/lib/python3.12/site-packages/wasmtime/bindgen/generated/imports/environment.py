from abc import abstractmethod
from typing import List, Protocol, Tuple

class HostEnvironment(Protocol):
    @abstractmethod
    def get_environment(self) -> List[Tuple[str, str]]:
        raise NotImplementedError


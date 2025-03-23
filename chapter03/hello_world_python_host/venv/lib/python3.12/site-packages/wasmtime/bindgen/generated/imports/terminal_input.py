from abc import abstractmethod
from typing import Protocol

TerminalInput = int
class HostTerminalInput(Protocol):
    @abstractmethod
    def drop_terminal_input(self, this: TerminalInput) -> None:
        raise NotImplementedError


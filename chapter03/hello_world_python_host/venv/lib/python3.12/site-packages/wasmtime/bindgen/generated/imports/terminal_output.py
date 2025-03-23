from abc import abstractmethod
from typing import Protocol

TerminalOutput = int
class HostTerminalOutput(Protocol):
    @abstractmethod
    def drop_terminal_output(self, this: TerminalOutput) -> None:
        raise NotImplementedError


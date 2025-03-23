from ..imports import terminal_input
from abc import abstractmethod
from typing import Optional, Protocol

TerminalInput = terminal_input.TerminalInput
class HostTerminalStdin(Protocol):
    @abstractmethod
    def get_terminal_stdin(self) -> Optional[TerminalInput]:
        raise NotImplementedError


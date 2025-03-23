from ..imports import terminal_output
from abc import abstractmethod
from typing import Optional, Protocol

TerminalOutput = terminal_output.TerminalOutput
class HostTerminalStderr(Protocol):
    @abstractmethod
    def get_terminal_stderr(self) -> Optional[TerminalOutput]:
        raise NotImplementedError


from ..imports import terminal_output
from abc import abstractmethod
from typing import Optional, Protocol

TerminalOutput = terminal_output.TerminalOutput
class HostTerminalStdout(Protocol):
    @abstractmethod
    def get_terminal_stdout(self) -> Optional[TerminalOutput]:
        raise NotImplementedError


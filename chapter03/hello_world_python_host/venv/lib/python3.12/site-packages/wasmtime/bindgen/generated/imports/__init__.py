from .environment import HostEnvironment
from .exit import HostExit
from .preopens import HostPreopens
from .random import HostRandom
from .stderr import HostStderr
from .stdin import HostStdin
from .stdout import HostStdout
from .streams import HostStreams
from .terminal_input import HostTerminalInput
from .terminal_output import HostTerminalOutput
from .terminal_stderr import HostTerminalStderr
from .terminal_stdin import HostTerminalStdin
from .terminal_stdout import HostTerminalStdout
from .types import HostTypes
from dataclasses import dataclass

@dataclass
class RootImports:
    streams: HostStreams
    types: HostTypes
    preopens: HostPreopens
    random: HostRandom
    environment: HostEnvironment
    exit: HostExit
    stdin: HostStdin
    stdout: HostStdout
    stderr: HostStderr
    terminal_input: HostTerminalInput
    terminal_output: HostTerminalOutput
    terminal_stdin: HostTerminalStdin
    terminal_stdout: HostTerminalStdout
    terminal_stderr: HostTerminalStderr

import os
import sys
from typing import Any, Callable, Dict, Optional, Text, TypeVar, Union

def run(statement: str, filename: Optional[str] = ..., sort: Union[str, int] = ...) -> None: ...
def runctx(statement: str, globals: Dict[str, Any], locals: Dict[str, Any], filename: Optional[str] = ..., sort: Union[str, int] = ...) -> None: ...

_SelfT = TypeVar('_SelfT', bound=Profile)
_T = TypeVar('_T')
if sys.version_info >= (3, 6):
    _Path = Union[bytes, Text, os.PathLike[Any]]
else:
    _Path = Union[bytes, Text]

class Profile:
    def __init__(self, timer: Callable[[], float] = ..., timeunit: float = ..., subcalls: bool = ..., builtins: bool = ...) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def print_stats(self, sort: Union[str, int] = ...) -> None: ...
    def dump_stats(self, file: _Path) -> None: ...
    def create_stats(self) -> None: ...
    def run(self: _SelfT, cmd: str) -> _SelfT: ...
    def runctx(self: _SelfT, cmd: str, globals: Dict[str, Any], locals: Dict[str, Any]) -> _SelfT: ...
    def runcall(self, func: Callable[..., _T], *args: Any, **kw: Any) -> _T: ...
    if sys.version_info >= (3, 8):
        def __enter__(self: _SelfT) -> _SelfT: ...
        def __exit__(self, *exc_info: Any) -> None: ...

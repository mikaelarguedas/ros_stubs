import threading
from typing import overload

import genpy

class Duration(genpy.Duration):
    @overload
    def __init__(self, secs: float = ...) -> None: ...
    @overload
    def __init__(self, secs: int = ..., nsecs: int = ...) -> None: ...

class Time(genpy.Time):
    @overload
    def __init__(self, secs: float = ...) -> None: ...
    @overload
    def __init__(self, secs: int = ..., nsecs: int = ...) -> None: ...
    @staticmethod
    def now() -> "Time": ...
    @classmethod
    def from_seconds(cls, float_secs: float) -> "Time": ...

def get_rostime() -> Time: ...
def get_time() -> float: ...
def set_rostime_initialized(val: bool) -> None: ...
def is_rostime_initialized() -> bool: ...
def get_rostime_cond() -> threading.Cond: ...
def is_wallclock() -> bool: ...
def switch_to_wallclock() -> None: ...
def wallsleep(duration: float) -> None: ...

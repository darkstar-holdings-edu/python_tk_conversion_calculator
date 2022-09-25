from typing import Callable, overload
from tkinter import Button, Entry, Label, Tk

__all__ = ["App"]

class App:
    window: Tk
    def __init__(self) -> None: ...
    def create_button(
        self, arg: str, row_pos: int, column_pos: int, callback: Callable[[], None]
    ) -> Button: ...
    def mainloop(self) -> None: ...
    @overload
    def create_label(self, arg: str, row_pos: int, column_pos: int) -> Label: ...
    @overload
    def create_label(
        self, arg: str, row_pos: int, column_pos: int, font: tuple[str]
    ) -> Label: ...
    @overload
    def create_label(
        self, arg: str, row_pos: int, column_pos: int, font: tuple[str, int]
    ) -> Label: ...
    @overload
    def create_label(
        self, arg: str, row_pos: int, column_pos: int, font: tuple[str, int, str]
    ) -> Label: ...
    def create_entry(self, width: int, row_pos: int, column_pos: int) -> Entry: ...

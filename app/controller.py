from tkinter import Button, Entry, Label, Tk
from typing import Callable

APP_NAME = "Conversion Calculator"


class App:
    window: Tk

    def __init__(self) -> None:
        super().__init__()

        window = Tk()
        window.title(APP_NAME)
        window.minsize(width=300, height=150)
        window.config(padx=10, pady=10)
        self.window = window

    def mainloop(self) -> None:
        """
        Wrapper to tk.mainloop() function. Call it just
        as you would if using Tk directly.
        """
        self.window.mainloop()

    def create_button(
        self,
        arg: str,
        row_pos: int,
        column_pos: int,
        callback: Callable[[], None],
    ) -> Button:
        """
        Creates a Tk button widget
        """
        button = Button()
        button.config(text=arg, command=callback)
        button.grid(row=row_pos, column=column_pos)

        return button

    def create_label(
        self,
        arg: str,
        row_pos: int,
        column_pos: int,
        font: tuple = ("Arial", 20, "normal"),
    ) -> Label:
        """
        Creates a Tk label widget
        """
        label = Label(text=arg, font=font)
        label.grid(row=row_pos, column=column_pos)

        return label

    def create_entry(self, width: int, row_pos: int, column_pos: int) -> Entry:
        """
        Creates a Tk entry (text box) widget
        """
        entry = Entry(width=width)
        entry.grid(row=row_pos, column=column_pos)

        return entry


if __name__ == "__main__":
    app = App()
    app.mainloop()

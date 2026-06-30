
"""AppFrame for <app_title>."""
import tkinter as tk
from tkinter import ttk
from pathlib import Path

from psiutils.constants import PAD
from psiutils.buttons import ButtonFrame
from psiutils.utilities import window_resize

from <app_name>.constants import APP_TITLE
from <app_name>.config import read_config
from <app_name>.text import Text

from <app_name>.main_menu import MainMenu
# from <app_name>.forms.frm

txt = Text()


class AppFrame():
    """Create AppFrame for <app_title> application."""
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.config = read_config()

        # tk variables
        # self.xxx = tk.StringVar()

        # Trace
        # self.xxx.trace_add('write', self._value_changed)

        self._show()

    def _show(self):
        root = self.root
        root.geometry(self.config.geometry[Path(__file__).stem])
        root.title(APP_TITLE)

        root.bind('<Control-x>', self._dismiss)
        root.bind('<Control-o>', self._process)
        root.bind('<Configure>',
                  lambda event, arg=None: window_resize(self, __file__))

        main_menu = MainMenu(self)
        main_menu.create()

        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)

        main_frame = self._main_frame(root)
        main_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=PAD, pady=PAD)

        self.button_frame = self._button_frame(root)
        self.button_frame.grid(row=8, column=0, columnspan=9,
                               sticky=tk.EW, padx=PAD, pady=PAD)

        sizegrip = ttk.Sizegrip(root)
        sizegrip.grid(sticky=tk.SE)

    def _main_frame(self, master: tk.Frame) -> ttk.Frame:
        frame = ttk.Frame(master)
        # frame.rowconfigure(0, weight=1)
        # frame.columnconfigure(0, weight=1)

        return frame

    def _button_frame(self, master: tk.Frame) -> tk.Frame:
        frame = ButtonFrame(master, tk.HORIZONTAL)
        frame.buttons = [
            frame.icon_button('build', self._process, True),
            frame.icon_button('close', self._dismiss),
        ]
        frame.enable(False)
        return frame

    def _value_changed(self) -> bool:
        """
        Determine whether any configuration value has changed.
        """
        enable = (
            self.xxx.get() != self.config.xxx
        )
        self.button_frame.enable(enable)

    def _process(self, *args) -> None:
        pass

    def _dismiss(self, *args) -> None:
        self.root.destroy()

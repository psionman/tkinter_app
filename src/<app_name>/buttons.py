# buttons.py
import tkinter as tk

from psiutils.buttons import ButtonFrame as ButtonFrameBase

ICON_BUTTON_PATH = "/home/jeff/.config/icon_buttons/buttons.json"
ICON_PATH = "/home/jeff/.local/share/psi_icons/"


class ButtonFrame(ButtonFrameBase):
    def __init__(
        self,
        master: tk.Frame,
        orientation: str = tk.HORIZONTAL,
        button_config_path: str = ICON_BUTTON_PATH,
        icon_path: str = ICON_PATH,
        **kwargs: dict,
    ):
        super().__init__(
            master,
            orientation,
            button_config_path,
            icon_path=icon_path,
            **kwargs,
        )

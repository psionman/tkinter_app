# config.py

"""Config for <app_title>."""

import tkinter as tk
from dataclasses import dataclass

from psiconfig import TomlConfig

from <app_name>.constants import CONFIG_PATH, USER_DATA_DIR


@dataclass
class ConfigField:
    type: type
    default_value: any


FIELDS = {
    "data_directory": ConfigField(tk.StringVar, USER_DATA_DIR),
}

DEFAULT_GEOMETRY = {
    "frm_main": "500x600",
    "frm_config": "700x300",
}

DEFAULT_CONFIG = {
    "geometry": DEFAULT_GEOMETRY,
}

for name, field in FIELDS.items():
    DEFAULT_CONFIG[name] = field.default_value

def read_config(restore_defaults: bool = False) -> TomlConfig:
    """Return the config file."""
    return TomlConfig(
        path=CONFIG_PATH,
        defaults=DEFAULT_CONFIG,
        restore_defaults=restore_defaults)


def save_config(updated_config: TomlConfig) -> TomlConfig | None:
    """Save the config file."""
    result = updated_config.save()
    if result != updated_config.STATUS_OK:
        return None
    return TomlConfig(CONFIG_PATH)


# Module-level singleton (TomlConfig) - this is the instance everyone imports.
config = read_config()

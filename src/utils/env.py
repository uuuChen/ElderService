import os
from dotenv import (
    load_dotenv,
)
from pathlib import Path
from typing import (
    List,
)


def get_project_root() -> str:
    # ----------------------------
    # root
    # |
    # └───src
    # │   |
    # |   |───utils
    # |   │     │
    # |   │     │───env.py
    # ----------------------------
    return str(Path(__file__).parent.parent.parent.resolve())


def load_os_environ():
    load_dotenv(os.path.join(get_project_root(), '.env'))


def make_sure_dirs_exist(dirs_path: List[str]):
    for path in dirs_path:
        os.makedirs(path, exist_ok=True)

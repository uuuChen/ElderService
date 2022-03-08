import os
from dotenv import (
    load_dotenv,
)
from pathlib import Path
from typing import (
    List,
    Set,
    Dict,
    Tuple,
    Optional,
)

def get_project_root() -> str:
    # ----------------------------
    # root
    # |
    # └───elder_service
    #     |
    #     └───src
    #     │   |
    #     |   |───utils
    #     |   │     │
    #     |   │     │───env.py
    # ----------------------------
    return str(Path(__file__).parent.parent.parent.parent.resolve())


def load_os_environ() -> None:
    load_dotenv(os.path.join(get_project_root(), '.env'))


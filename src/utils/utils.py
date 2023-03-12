from typing import (
    List,
    Dict,
    Type,
)
import os

def are_all_vals_none(vals: List[any]) -> bool:
    return all(v is None for v in vals)


def are_all_vals_not_none(vals: List[any]) -> bool:
    return all(v is not None for v in vals)


def if_raise(condition: bool, exception: Type[Exception], error_str: str = ""):
    if condition:
        raise exception(error_str)


def pop_required_args(keys: List[any], d: Dict[any, any]) -> List[any]:
    ret = list()
    for key in keys:
        if_raise(key not in d, ValueError, f"argument [{key}] is required")
        ret.append(d.pop(key))
    return ret


def make_sure_dirs_exist(dirs_path: List[str]):
    for path in dirs_path:
        os.makedirs(path, exist_ok=True)

class DotDict(dict):
    """
    This is a class that inherits dict, and it can use dot to access dict values.
    Reference: https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary    
    """    
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


from typing import (
    List,
    Dict,
)


def are_all_vals_none(vals: List[any]) -> bool:
    return all(v is None for v in vals)


def are_all_vals_not_none(vals: List[any]) -> bool:
    return all(v is not None for v in vals)


def get_parse_args(target_args: List[str], **kwargs) -> Dict[str, any]:
    ret = DotDict(dict())
    for key in target_args:
        ret[key] = kwargs.get(key, None)
    return ret


class DotDict(dict):
    """
    This is a class that inherits dict, and it can use dot to access dict values.
    Reference: https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary    
    """    
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


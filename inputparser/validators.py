
import re
from typing import Union, Callable


def in_list(val, allowable, case_sensitive: bool = False) -> bool:
    """
    Check if provided value is in the allowable list

    Args:
        val : value to check. Can be of any type
        allowable: list (or single element) to compare the val field to
        case_sensitive: boolean flag for use when comparing strings
    """

    # Force any single element allowable args to be a list
    if not isinstance(allowable, list):
        allowable = [allowable]

    # If the results are not case-sensitive, force comparison
    # on lower-case, so the user does not get an error from using caps
    if isinstance(val, str) and not case_sensitive:
        val = val.lower()

    return val in allowable


def is_real(val) -> bool:
    """
    Check if the provided argument is real
    :param val: value to check
    :return: boolean indicating value is real
    """
    return False if isinstance(val, complex) else True


def is_positive(val) -> bool:
    """
    Check if the provided argument is real and positive

    :param val: value to check
    :return: boolean indicating value is positive
    """
    return is_real(val) and val >= 0


def in_range(val, allowable_range: tuple, inclusive: bool = True) -> bool:
    """
    Check if the provided val is within the specified range

    Args:
        val : int or float to check
        allowable_range : tuple specifying the min and max value
        inclusive : boolean flag to specify if the value can be equal to
            the provided min and max range. Default of True means if the value
            is equal to the min or max, the function returns True
    """
    max_val = max(allowable_range)
    min_val = min(allowable_range)

    if not is_real(val):
        return False

    if inclusive:
        does_pass = min_val <= val <= max_val
    else:
        does_pass = min_val < val < max_val

    return does_pass


def are_valid_elements(vals: list, element_constraint: Callable, args=[], constraint_args={}) -> bool:
    """
    Check if the elements of a list conform to the provided constraint

    Args:
        vals : list of values to iterate through and check
        element_constraint : function reference used to check each element of the list
        constraint_args : dictionary of keyword arguments to pass to the element
            constraint function. Default to empty dict.
    """
    does_pass = isinstance(vals, list)
    for val in vals:
        does_pass &= element_constraint(val, *args, **constraint_args)

    return does_pass


def matches_reg_ex(val, reg_ex: str):
    """
    Check if the provided argument matches the provided regular expression

    :param val: value to check
    :param reg_ex: regular expression string to compare the value to
    """
    return bool(re.fullmatch(reg_ex, val))


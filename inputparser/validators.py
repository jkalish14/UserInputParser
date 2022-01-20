
import re
from typing import Union, Callable, Tuple


def in_list(val: list, allowable: list, case_sensitive: bool = False) -> bool:
    """
    Check if provided value is in the allowable list

    :param val: value to check
    :param allowable: list of arguments that are allowable
    :param case_sensitive: flag to enforce case sensitivity when the val is a string
    :return: boolean indicating if the val was in the allowable list
    """

    # Force any single element allowable args to be a list
    if not isinstance(allowable, list):
        allowable = [allowable]

    # If the results are not case-sensitive, force comparison
    # on lower-case, so the user does not get an error from using caps
    if isinstance(val, str) and not case_sensitive:
        val = val.lower()

    return val in allowable


def is_real(val: (int, float)) -> bool:
    """
    Check if the provided argument is real

    :param val: value to check
    :return: boolean indicating value is real
    """
    return False if isinstance(val, complex) else True


def is_positive(val: (int, float)) -> bool:
    """
    Check if the provided argument is real and positive

    :param val: value to check
    :return: boolean indicating value is positive
    """
    return is_real(val) and val >= 0


def in_range(val: (int, float), allowable_range: Tuple, inclusive: bool = True) -> bool:
    """
    Check if the provided value is within the allowable range

    :param val: value to check
    :param allowable_range: iterator specifying the min and max allowable values
    :param inclusive: flag to specify if the value can be equal to the provided min and max range.
        Default of True means if the value is equal to the min or max, the function returns true
    :return: boolean flag indicating the value is within the range
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
    Check if the elements of a list conform ot the provided constraint function

    :param vals: list of values to check against the constraint
    :param element_constraint: function handle used to check each element
    :param args: positional arguments to pass into the element_constraint function
    :param constraint_args: keyword arguments to pass into the element_constraint function
    :return: boolean flag indicating each element in the list meets the constraint
    """

    does_pass = isinstance(vals, list)
    for val in vals:
        does_pass &= element_constraint(val, *args, **constraint_args)

    return does_pass


def matches_reg_ex(val: str, reg_ex: str) -> bool:
    """
    Check if the provided argument matches the provided regular expression

    :param val: value to check
    :param reg_ex: regular expression string to compare the value to
    :return: boolean flag indicating a match
    """
    return bool(re.fullmatch(reg_ex, val))


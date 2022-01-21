
from inputparser import *


def evaluate_test_case(parser: InputParser, user_arg, expected_result: bool):
    assert parser.is_valid(user_arg, supress_error=True) is expected_result, f"Test Case for {user_arg} failed. Expected value was {expected_result}"


def test_boolean():
    default_value = True
    parser = InputParser(default_value, bool)

    test_cases = [(True, True), (False, True), ("1", False)]
    for case in test_cases:
        evaluate_test_case(parser, case[0], case[1])


def test_is_in_list():
    default_value = 10
    parser = InputParser(default_value, int, in_list, {"allowable": [10, 20, 30, 40]})
    parser2 = InputParser(default_value, int, in_list, {"allowable": 20})

    test_cases = [(20, True), (22, False), ("22", False)]
    for case in test_cases:
        evaluate_test_case(parser, case[0], case[1])
        evaluate_test_case(parser2, case[0], case[1])



def test_is_real():
    default_value = 10
    parser = InputParser(0, (int, float, complex), is_real)

    test_cases = [(20, True), (-3, True), (3j, False)]
    for case in test_cases:
        evaluate_test_case(parser, case[0], case[1])


def test_is_positive():
    default_value = 1.0
    parser = InputParser(default_value, (float, int), is_positive)

    test_cases = [(1, True), (1.0, True), (0.0, True), (-1, False), (False, True)]
    for case in test_cases:
        evaluate_test_case(parser, case[0], case[1])


def test_in_range_noninclusive():
    default_value = 0.125
    parser = InputParser(default_value, (float, int), in_range, {"allowable_range": (0, 1), "inclusive": False})

    test_cases = [(1, False), (1.0, False), (0.0, False), (-1, False), (0.2, True), ("12", False)]
    for tup in test_cases:
        evaluate_test_case(parser, tup[0], tup[1])


def test_in_range_inclusive():
    default_value = 0.125
    parser = InputParser(default_value, (float, int, complex), in_range, {"allowable_range": (0, 1), "inclusive": True})

    test_cases = [(1, True), (1.0, True), (0.0, True), (-1, False), (0.2, True), ("12", False), (2j, False)]
    for case in test_cases:
        evaluate_test_case(parser, case[0], case[1])


def test_are_elements_positive():
    default_value = [10, 20, 30]
    parser = InputParser(default_value, (float, int), are_valid_elements, {"element_constraint": is_positive})

    test_cases = [([-3, 4, 2], False), ([1, 2, 3], True), (["1", 2, 3], False), ([1, "2"], False)]
    for case in test_cases:
        evaluate_test_case(parser, case[0], case[1])


def test_are_elements_in_range():
    default_value = [10, 20, 30]
    parser = InputParser(default_value, (float, int),
                         are_valid_elements,
                         {"element_constraint": in_range,
                          "constraint_args": {"allowable_range": (-2, 3)}})

    test_cases = [([-3, 4, 2], False), ([1, 2, 3], True), (["1", 2, 3], False), ([1, "2"], False)]
    for case in test_cases:
        evaluate_test_case(parser, case[0], case[1])


def test_are_elements_in_list():
    default_value = 1
    parser = InputParser(default_value, (float, int, str),
                         are_valid_elements,
                         {"element_constraint": in_list,
                          "constraint_args": {"allowable": [1, 2, 3, "3"]}})

    test_cases = [([-3, 4, 2], False), ([1, 2, 3], True), (["1", 2, 3], False), ([1, "3"], True)]
    for case in test_cases:
        evaluate_test_case(parser, case[0], case[1])


def test_matches_reg_ex():
    # Regular Expression source https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    reg_ex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    default_value = None

    parser = InputParser(default_value, str, matches_reg_ex, {"reg_ex" : reg_ex})

    test_cases = [("hassdfgas@gmail.com", True), ("15afsd@hotmail.com", True), ("TESTING@gmail.com", True), ("123", False)]
    for case in test_cases:
        evaluate_test_case(parser, case[0], case[1])


def test_lambda():
    default_value = 1
    parser = InputParser(default_value, (float, int), lambda x: x > 10)
    test_cases = [(10, False), (9.0, False), (11.0, True), ("2", False), (True, False)]
    for case in test_cases:
        evaluate_test_case(parser, case[0], case[1])


def test_user_input_error():
    error = None
    usr_arg = -0.2
    validator_function = is_positive
    parser = InputParser(1, (float, int), validator_function)

    try:
        val = parser.is_valid(usr_arg)
    except UserInputError as e:
        error = e

    passing = True
    passing &= isinstance(error, UserInputError)
    passing &= str(usr_arg) in error.message
    passing &= validator_function.__name__ in error.message
    assert passing

def test_properties():
    failing_arg = -0.2
    passing_arg = 3
    default_arg = 1
    validator_function = is_positive
    parser = InputParser(default_arg, (float, int), validator_function)

    parser.is_valid(failing_arg, supress_error=True)

    passing = True
    passing &= parser.user_arg == failing_arg
    passing &= parser.default == default_arg
    passing &= parser.value == default_arg
    passing &= parser.valid is False
    passing &= len(parser.error_str) > 0

    parser.is_valid(passing_arg)

    passing &= parser.value == passing_arg

    assert passing
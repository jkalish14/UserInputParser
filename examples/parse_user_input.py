import warnings
from inputparser import *
import json

from inputparser import InputParser


def custom_constraint(val, str_starts_with: str):
    returnValue = True
    if len(val) < len(str_starts_with):
        returnValue = False
    elif val[0:len(str_starts_with)] == str_starts_with:
        returnValue = True

    return returnValue


settings_template = {
    "account": InputParser("Chase", str),
    "account_type": InputParser("checkings", str, in_list, {"allowable": ["checkings", "savings"],
                                                            "case_sensitive": False}),
    "balance": InputParser("$0", str, custom_constraint, {"str_starts_with": "$"}),
    "previous_interest_rates": InputParser([], (int, float), are_valid_elements, {"element_constraint": in_range,
                                                                                  "constraint_args":
                                                                                      {"allowable_range": (0.0, 0.1)}
                                                                                  }),

    "interest_rate": InputParser(0.0, float, in_range, {"allowable_range": (0.0, 0.1), "inclusive": True}),
    "account_number": InputParser(None, str, lambda x: len(x) == 9)
}

# Load the user's settings file
file_name = "./examples/user_input_example.json"
file = open(file_name)
user_data = json.load(file)

# Iterate over the keys and check if the inputs are valid
for k, v in dict(user_data).items():

    parser: InputParser = settings_template[k]

    try:
        parser.is_valid(v)
    except UserInputError as e:
        # Catch the error and prefix the error message with the name of the invalid field
        error_string = [f"\nUser value provided for {k} in {file_name} is invalid: \n"]
        error_string += e.message
        error_string += f"\nUsing default value of {parser.default}"
        warnings.warn("".join(error_string))
        user_data[k] = parser.default

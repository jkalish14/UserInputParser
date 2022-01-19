
from typing import Any, Tuple
from inputparser.validators import *


class UserInputError(Exception):
    """
    Error message that gets raised when a user input is invalid
    """

    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(message)


class InputParser:

    def __init__(self, default_val, allowable_types: Union[type, Tuple], constraint_func: Callable = None,
                 constraint_args=None):
        """
        Create a new User Input Checker to ensure inputs from the user are valid.

        :param default_val: If there is an error with the user's input, this is the value the field will default to
        :param allowable_types: type, or tuple of types that the input argument can be
        :param constraint_func: function reference that will be used to validate the user's input
        :param constraint_args: dictionary of arguments to be passed to the logic_check function. Dictionary
                keys must match logic_check function keyword arguments.
        """
        if constraint_args is None:
            constraint_args = {}
        self.__default_arg = default_val
        self.__allowable_types = allowable_types
        self.__check_callback: Callable = constraint_func
        self.__callback_args: dict = constraint_args
        self.__error_str: str = ""
        self.__user_arg = None
        self.__valid: bool = False
        self.__value: Any = None

    @property
    def value(self) -> Any:
        return self.__value

    @property
    def default(self):
        """
        Get the default argument provided by the user

        :return: specified default argument
        """
        return self.__default_arg

    @property
    def valid(self) -> bool:
        """
        Get the boolean flag indicating if the user's input was valid.
        Note, this field is None until is_valid() is called

        :return: boolean flag indicating valid user argument
        """
        return self.__valid

    @property
    def user_arg(self):
        """
        Get the original argument provided by the user

        :return: user's input argument
        """
        return self.__user_arg

    @property
    def error_str(self) -> str:
        """
        Get the warning string that is constructed when a user's input is invalid

        :return: error string
        """
        return self.__error_str

    def __validate_type(self, user_arg: Union[Any, list]) -> bool:

        # Check each element of a list
        if isinstance(user_arg, list):
            does_pass = are_valid_elements(user_arg, isinstance, [self.__allowable_types])
        else:
            does_pass = isinstance(user_arg, self.__allowable_types)

        return does_pass

    def __print_error(self, supress):
        if not supress:
            raise UserInputError(self.__error_str)

    def is_valid(self, user_arg, supress_error: bool = False) -> bool:
        """
        Take the provided user_arg and run it through the logic_check function
        """

        # Save the provided user arg in case it is needed for error messages
        self.__user_arg = user_arg
        self.__value = user_arg
        self.__valid = True

        # Compare the user_arg with the list of acceptable types
        # If no check callback is provided, the type verification
        # is sufficient
        if self.__validate_type(user_arg) is False:
            warning_string = [f"Provided value of \'{user_arg}\' is of type \'{type(user_arg)}\'. \n"]
            warning_string += ["\t" * 1 + f"Value for this field must be one of the following types: \n"]
            warning_string += ["\t" * 2 + f"- {t} \n" for t in self.__allowable_types] if \
                isinstance(self.__allowable_types, list) else \
                ["\t" * 5 + f"- {self.__allowable_types} \n"]

            self.__error_str = "".join(warning_string)
            self.__valid = False
            self.__value = self.__default_arg
            self.__print_error(supress_error)

        elif self.__check_callback is not None:
            self.__valid = self.__check_callback(user_arg, **self.__callback_args)

            if self.__valid is False:
                # Create the warning
                warning_string = [
                    f"Provided value of \'{user_arg}\' did not meet the constraints enforced by: "
                    f"{self.__check_callback.__name__}(). \n"]

                if self.__callback_args is not None:
                    warning_string += ["\t" * 1 + "Arguments passed to constraint function: \n"]
                    warning_string += ["\t" * 2 + f"- {k} : {v.__name__ if isinstance(v, Callable) else v} \n" for k, v
                                       in self.__callback_args.items()]

                # Join the lists of messages together and assign
                self.__error_str = "".join(warning_string)
                self.__value = self.__default_arg
                self.__print_error(supress_error)

        # We only get here if everything is okay
        return self.__valid



# Features
## Powerful

Type checking is included by default. If you need something more complex, that's supported too.

Evaluate elements of a list to ensure they meet your specific conditions
```python
from inputparser import *

InputParser(default_val=[], 
            allowable_types=(int, float), 
            constraint_func=are_valid_elements, 
            constraint_args={"element_constraint": in_range,
                             "constraint_args":
                                   {"allowable_range": (0.0, 0.1)}
                            })
```

or perhaps you want something custom. Provide your own constraint function:
```python
from inputparser import *

# Define your own constraint function
def custom_constraint(val, str_starts_with: str):
    returnValue = True
    if len(val) < len(str_starts_with):
        returnValue = False
    elif val[0:len(str_starts_with)] == str_starts_with:
        returnValue = True

    return returnValue

# Create the object 
parser = InputParser(default_val="$0", 
                     allowable_types=str, 
                     constraint_func=custom_constraint, 
                     constraint_args={"str_starts_with": "$"})
```

## Helpful Error Messages

As a user there is nothing more frustrating than not knowing why there is an error.
Or worse, not knowing why the program did not work as expected.

UserInputParser constructs helpful error messages that the developers can display to the user.
```
User value provided for previous_interest_rates in ./examples/user_input_example.json is invalid: 
Provided value of '[5000, 6000, 7000, 8000]' did not meet the constraints enforced by: are_valid_elements(). 
	Arguments passed to constraint function: 
		- element_constraint : in_range 
		- constraint_args : {'allowable_range': (0.0, 0.1)} 

Using default value of []
```

# Installation
```
pip install UserInputParser
```
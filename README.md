
<br />

<div align="center">
<h1>UserInputParser</h1>

</div>

<br />
<div align="center">
  <b>A python module to parse user's input and provide helpful error messages on failure</b>
</div>
<br />


<p align="center">
<img alt="GitHub" src="https://img.shields.io/github/license/jkalish14/UserInputParser?style=plastic">
</p>

---

# Features

## Powerful

Type checking is included by default. If you need something more complex, that's supported too.

Evaluate elements of a list to ensure they meet your specific conditions:
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

see more [example use-cases](./examples)


# Installation
```
pip install UserInputParser
```

Then import the package
```python
from inputparser import *
```

and get to checkin'

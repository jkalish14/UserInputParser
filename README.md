
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
<img src="https://img.shields.io/github/license/jkalish14/UserInputParser"/>
<a href='https://userinputparser.readthedocs.io/en/latest/?badge=latest'><img src='https://readthedocs.org/projects/userinputparser/badge/?version=latest' alt='Documentation Status' />
<a href="https://github.com/jkalish14/UserInputParser/actions/workflows/Test.yml"><img src="https://github.com/jkalish14/UserInputParser/actions/workflows/Test.yml/badge.svg"/>
<img src="https://sonarcloud.io/api/project_badges/measure?project=jkalish14_UserInputParser&metric=sqale_rating"/>
<img src="https://sonarcloud.io/api/project_badges/measure?project=jkalish14_UserInputParser&metric=reliability_rating"/>
</p>

<p align="center">
    <a target="_blank" href="https://userinputparser.readthedocs.io/en/latest/">Documentation</a>
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

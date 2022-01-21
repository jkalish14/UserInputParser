
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
<img src="https://sonarcloud.io/api/project_badges/measure?project=jkalish14_UserInputParser&metric=coverage"/>
</p>

<p align="center">
    <a target="_blank" href="https://userinputparser.readthedocs.io/en/latest/">Read The Documentation</a>
  </p>

---

# Usage

## Installation
```
pip install UserInputParser
```

Then import the package

```python
from inputparser import *
```
This will make InputParser avalaible as well as all the natively supported validator functions.

## Basic Example
```python
from inputparser import *

parser = InputParser("", str, in_list, {"allowable" : ["a", "b", "c", "d"]})

valid = parser.is_valid(input("Select an option: a, b, c, d"))

```
and on error...
```
inputparser.inputparser.UserInputError: Provided value of 'e' did not meet the constraints enforced by: in_list(). 
	Arguments passed to constraint function: 
		- allowable : ['a', 'b', 'c', 'd'] 
```

see more [example use-cases](https://github.com/jkalish14/UserInputParser/tree/master/examples)

# Features

## Extensible

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
    return True if val[0:len(str_starts_with)] == str_starts_with else False

# Create the object 
parser = InputParser(default_val="$0", 
                     allowable_types=str, 
                     constraint_func=custom_constraint, 
                     constraint_args={"str_starts_with": "$"})
```


## Helpful Error Messages

As a user, not knowing where or why your input was wrong is aweful. Or worse, having the program produce wrong
results because the user entered a percentage instead of a decimal - but didn't error.
```
User value provided for interest_rate in ./examples/user_input_example.json is invalid: 
Provided value of '0.2' did not meet the constraints enforced by: in_range(). 
	Arguments passed to constraint function: 
		- allowable_range : (0.0, 0.1) 
		- inclusive : True 

Using default value of 0.0
```

This even works for custom functions.

## Lightweight

UserInputParser has no dependencies to keep your programs fast.
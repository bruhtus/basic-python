### Report

#### MOdule

##### OS module
> perform operatinng system task.

example:

```python
import os

os.mkdir('directory_name') #create directory
os.chdir('path') #change current directory
os.getcwd() #get current working directory
os.rmdir() #removing directory
```

##### Sys module
> provides functions and variables used to manipulate different parts of the python runtime environment.

`sys.argv` returns a list of command line arguments passed to a python script. the item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.

example:
```python
sys.exit() #to exit sys
sys.maxsize #to know the largest integer variable it takes
sys.path #to know environment path
sys.version #to know the version of python you are using
```

##### Statistics module
> provides functions for mathematical statistics of numeric data.

example:
```python
from statistics import * #importing all the statistics modules
ages = [20, 30, 69]

print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))
```

##### Math module
> containing many mathematical operations and constants.

example:

```python
import math

print(math.pi) #pi constant
print(math.sqrt(2)) #square root (bahasa: pangkat)
print(math.pow(2, 3)) #exponential function
print(math.floor(9.81)) #rounding to lowest
print(math.ceil(9.81)) #rounding to highest
print(math.log10(100)) #logarithm with 10 as base
```

##### String module

example:

```python
import string

print(string.ascii_letters) #abcdefghijkl...
print(string.digits) #0123456789
print(string.punctuation) #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

##### Random module
> give random instances

example:

```python
from random import random, randint

print(random()) #doesn't take any arguments, it returns a value between 0 and 0.9999
print(randint(5, 20)) #it returns a random integer number between 5 and 20
```

#### List comprehension
> a compact way of creating a list from a sequence. short way to create a new list.

#### Function
- [functions as parameters](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/14_Day_Higher_order_functions/14_higher_order_functions.md#function-as-a-parameter)
- [returning functions as return value from other functions](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/14_Day_Higher_order_functions/14_higher_order_functions.md#function-as-a-return-value)
- using python closures and decorators (closures: nested functions, decorator is a design pattern that allows a user to add new functionality to an existing object without modifying its structure)

`map()` function is a built-in function that takes a function and iterable as parameters. syntax: `map(function, iterable)`.

`filter()` function calls the specified function which returns boolean for each item of the specified iterable (list). it filters the items that satisfy the filtering criteria.

### Report

- with continue statement we can stop the current iteration and continue with the next iteration.
- the range() function is used to loop through a set of code a certain number of times. `range(start, end, step)`. the range sequence needs at least 1 argument `(end)`.
- for some reason, i can't use `[range(n)]` to initialize list with `range` function but i can use `list(range(n))`.

#### Function

> when we make a function, we call it declaring a function. when we start using it, we call it calling or invoking a function. function can be declared with or without parameters.
- If we do not pass arguments when calling the function, their default values will be used (if the function have default values).

- without paramaters:

```python
def function_name(): #declaring a function
    codes

function_name() #calling a function
```

- with parameters:

```python
def function_name(parameter): #declaring a function
    codes

function_name(parameter) #calling a function

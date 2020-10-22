This is 15 days of me learning the python basic again instead of doing an actual project. Basically back to basic.

Source:
- [30 days of python](https://github.com/Asabeneh/30-Days-Of-Python)
- [decorators](https://stackoverflow.com/a/1594484)

There're four collection data types in python:
- List: A collection which is ordered and changeable (modifiable). Allows duplicate members.
- Tuple: A collection which is ordered and unchangeable or unmodifiable. Allows duplicate members.
- Set: A collection which is unordered, unindexed, unmodifiable but you can add new items. No duplicate members.
- Dictionary: A collection which is unordered, changeable (modifiable), and indexed. No duplicate members.

If the processing logic require so, the sequential flow of execution can be altered in two way:
- Conditional execution: a block of one or more stetements will be executed if a certain expression is true.
- Repertitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true.

Function is a reuseable block of code or programming statements  designed to perform a certain task.

To define a function, python provides the `def` keyword. The function block of code is executed only if we call it.

Function can also return values, if a function does not return any, the value of the function is none.

If we don't know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding `*` before the parameters name.

A module is a file containing a single variable, or a function, or a big code base.

Lamda function is a small anonymous function without a name. It can take any number of arguments but can only have one expression. We need it when we want to write an anonymous function inside another function.

Function can perform these following operations:
- a function can take one or more functions as parameters
- a function can be returned as a result of another function
- a function can be modified
- a function can be assigned to a variable

Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it. <br>
Syntax:

```python
@wrapper
def function(n):
    statements(s)
```

That's similar to:

```python
def function(n):
    statement(s)

function = wrapper(function)
```

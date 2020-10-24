This is 15 days of me learning the python basic again instead of doing an actual project. Basically back to basic.

Source:
- [30 days of python](https://github.com/Asabeneh/30-Days-Of-Python)
- [Decorators](https://stackoverflow.com/a/1594484)

There're four collection data types in python:
- List: A collection which is ordered and changeable (modifiable). Allows duplicate members.
- Tuple: A collection which is ordered and unchangeable or unmodifiable. Allows duplicate members.
- Set: A collection which is unordered, unindexed, unmodifiable but you can add new items. No duplicate members.
- Dictionary: A collection which is unordered, changeable (modifiable), and indexed. No duplicate members.

If the processing logic require so, the sequential flow of execution can be altered in two way:
- Conditional execution: a block of one or more stetements will be executed if a certain expression is true.
- Repertitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true.

Using `*` means there's only one value (it basically save all the arguments into a tuple), that's why args using only `*` and the syntax be like `*args`. Using `**` means there're two value or to be precise a key and a value (it's basically save all the arguments into dictionary), that's why kwargs and dict using `**` and the syntax be like `**kwargs` and `**dict`. (args = arguments, kwargs = keyword arguments).

If we're interested in an index of a list, we use `enumerate`.

Use `zip` to combine lists when looping through them.

Function is a reuseable block of code or programming statements  designed to perform a certain task.

To define a function, python provides the `def` keyword. The function block of code is executed only if we call it.

Function can also return values, if a function does not return any, the value of the function is none.

If we don't know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding `*` before the parameters name.

A module is a file containing a single variable, or a function, or a big code base.

Lambda function is a small anonymous function without a name. It can take any number of arguments but can only have one expression. We need it when we want to write an anonymous function inside another function.

The differnce between `lambda` and `def` is that `def` used to define normal functions (need name) and `lambda` used to define anonymous functions (doesn't need a name).

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

variable = wrapper(function)
```

### The Difference Between Method and Function

1. Function and method both look similar as they perform in almost similar way, but the key difference is the concept of **Class and its Object**.
2. Funciton can be called **only by its name**, as it is defined independently. But methods **can't be called by its name only**, we need to invoke the class by a reference of that class in which it is defined. <br>
i.e. **method is defined within a class and hence they are dependent on that class**.

### Python Error Types

- SyntaxError: the syntax was wrong.
- NameError: variable name not defined.
- IndexError: usually index out of range (print index length first to check).
- ModuleNotFoundError: there's no such module.
- AttributeError: the module doesn't have such attribute or function.
- KeyError: basically a typo.
- TypeError: different data type (convert the data type first).
- ImportError: there's no such function in the module.
- ValueError: there's a problem with the value (whether it's not supported or something else).
- ZeroDivisionError: cannot divide a number by zero.

**ImportError: cannot import name 'datetime' from partially initialized module 'datetime' (most likely due to a circular import)** >> that happens because of the file name the same as the module name.

### Try and Except

![](try-except.png)

To analyze the problem, we can use different error types with except. For example: <br>
```python
try:
    print 'hello word'

except SyntaxError:
    print('the syntax is wrong')

else:
    print('forget about it')

finally:
    print('it is over')
```

### Regular Expressions

A regular expression or RegEx is a special text that helps to find patterns in data.

A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is called `re`.

#### Function in `re` Module

- `re.match()`: search *only in the beginning of the first line* of the string and returns matched objects if found, else returns none.
- `re.search`: return a match object if there is one anywhere in the string, including multiline strings.
- `re.findall`: return a list containing all matches.
- `re.split`: takes a string, splits it at the match points, returns a list.
- `re.sub`: replaces one or many matches within a string.

Example Syntax:

```python
re.match(substring, string, re.I)
#substring is a pattern
#string is the text we look for the pattern
#re.I is case ignore flag (ignore uppercase or lowercase)
```

For more info about RegEx or `re` module, you can check [here](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/18_Day_Regular_expressions/18_regular_expressions.md#writing-regex-patterns).

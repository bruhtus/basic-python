def hello_decorator(func1):
    def inner1():
        print('this is start wrapper')
        func1()
        print('this is end wrapper\n')

    return inner1

@hello_decorator
def function_used():
    print('this is the function 1 inside the wrapper')

function_used()

def another_decorator(function_to_decorator):
    def wrapper(arg1, arg2):
        print(f'I got args! look: {arg1}, {arg2}')
        function_to_decorator(arg1, arg2)

    return wrapper

@another_decorator
def print_fullname(firstname, lastname):
    print(f'My name is {firstname} {lastname}')

print_fullname('Robertus', 'Chris')

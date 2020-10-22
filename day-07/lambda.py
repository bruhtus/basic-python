add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))

print(f'self invoking lambda function: {(lambda a,b: a + b)(2,3)}')

def power(x):
    return lambda n: x**n

cube = power(2)(3) #need 2 arguments to run, in separate rounded brackets
print(cube)

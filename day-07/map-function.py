numbers = [1, 2, 3, 4, 5] #iterable

def square(x):
    return x ** 2

numbers_squared = map(square, numbers)
print(list(numbers_squared)) #must conver to list first

numbers_squared_2 = map(lambda x: x**2, numbers)
print(list(numbers_squared_2))

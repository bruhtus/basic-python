from functools import reduce

numbers = [1, 2, 3, 4, 5]

def add_two_nums(x, y):
    return x + y

total = reduce(add_two_nums, numbers)

print(total)

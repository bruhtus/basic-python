def sum_of_numbers(a, b, c, d, e):
    return a + b + c + d + e

numbers = range(2, 7)
print(list(numbers))
print(sum_of_numbers(*list(numbers)))

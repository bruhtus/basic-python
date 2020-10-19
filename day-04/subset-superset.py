numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {2, 4, 6, 8, 10}

print(f'is whole numbers subset of even numbers? {numbers.issubset(even_numbers)}')
print(f'is even numbers subset of whole numbers? {even_numbers.issubset(numbers)}\n')

print(f'is whole numbers superset of even numbers? {numbers.issuperset(even_numbers)}')
print(f'is even numbers superset of whole numbers? {even_numbers.issuperset(numbers)}\n')

ages = [12, 18, 35, 69, 80, 69, 69]

print(f'sorting list without modifying original list: {sorted(ages)}')
print(f'sorting list without modifying original list: {sorted(ages, reverse=True)}\n')

ages.sort()
print(f'sorting list (ascend): {ages}')

ages.sort(reverse=True)
print(f'sorting list (descend): {ages}')

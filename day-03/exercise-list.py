ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()

print(f'max: {max(ages)}')
print(f'min: {min(ages)}')

ages_min = min(ages)
ages_max = max(ages)
ages.append(ages_min)
ages.append(ages_max)
print(f'after append min and max: {ages}')

ages.sort()
print(f'after append min and max (sorted ascend): {ages}')
print(f'median: {(ages[6]+ages[7])/2}')

print(f'sum of list: {sum(ages)}')
print(f'average of list: {sum(ages)/2}')
print(f'range ages: {ages_max-ages_min}')

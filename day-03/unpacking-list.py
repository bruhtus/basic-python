lst = ['anu', 'ini', 'itu']

first, *rest = lst

print(f'unpacked the first: {first}')
print(f'unpacked the rest: {rest}\n')

lst_2 = ['anu', 'ini', 'itu', 'nganu', 'ngitu']

one, two, *rest_2, four, five = lst_2

print(f'unpacked the first one: {one}')
print(f'unpacked the second: {two}')
print(f'unpacked the four: {four}')
print(f'unpacked the fifth: {five}')
print(f'unpacked the rest: {rest_2}')

lst = ['anu', 'itu']
print(f'original list: {lst}')

lst_2 = lst.copy()
print(f'copy of original list: {lst_2}\n')

lst_2.append('ini')
print(f'copy of original list after append: {lst_2}')
print(f'original list: {lst}')

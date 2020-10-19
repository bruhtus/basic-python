tpl= ('anu', 'ini', 'itu')
print(f'before changing tuple to list: {type(tpl)}')

#tpl = list(tpl)
tpl = [tpl]
print(f'after changing tuple to list: {type(tpl)}')

tpl = tuple(tpl)
print(f'after changing list to tuple: {type(tpl)}')

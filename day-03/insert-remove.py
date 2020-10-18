fruits = ['banana', 'avocado', 'orange']
print(f'before insert items to list: {fruits}')

fruits.insert(2, 'lime') #(index, item)
print(f'after insert items to list: {fruits}')

fruits.remove('avocado')
print(f'after remove items from list: {fruits}')

fruits.pop(1) #(index)
print(f'after remove index one from list with pop: {fruits}')

fruits.pop() #remove the last item if index not specified
print(f'after remove last items from list with pop: {fruits}')

fruits.insert(2, 'lime') #(index, item)
fruits.insert(3, 'avocado') #(index, item)

del fruits[0]
print(f'after delete first items from list: {fruits}')

del fruits[1:]
print(f'after delete second and below items from list: {fruits}')

#del fruits #delete list completely

fruits.clear()
print(f'after clearing the list: {fruits}')

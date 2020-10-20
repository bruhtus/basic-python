fruits = ['banana', 'orange']
input_usr = input('what fruits you want in a list? ')

if input_usr in fruits:
    print(f'your fruit already in list, here check it out yourself: {fruits}')

else:
    fruits.append(input_usr)
    print(f'done: {fruits}')

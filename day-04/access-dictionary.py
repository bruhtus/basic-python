person = {
        'first_name': 'Robertus',
        'last_name': 'Chris',
        'age': 69,
        'skills': ['sotosop', 'lightroom'],
        'address': {
            'street': 'it is just tutorial',
            'zipcode': 'calm down'
            }
        }

print(f"my first name is: {person['first_name']}")
print(f"my address is: {person['address']}")
print(f"my address zipcode is: {person['address']['zipcode']}\n")

print(f"check if an item in the dictionary: {person.get('address')}")
print(f"check if an item in the dictionary: {person.get('city')}\n")

person['city'] = 'surabaya' #add item to dictionary
person['skills'].append('python')

print(f'after adding item: {person}\n')

person['address']['zipcode'] = 'not gonna input it, sorry' #changing specific dictionary
print(f"after changing zipcode: {person['address']['zipcode']}\n")

print(f"check city in dictionary: {'city' in person}")
print(f"check fetish in dictionary: {'fetish' in person}\n")

person['address'].pop('street')
print(f"delete address street in dictionary: {person['address']}")

person.popitem() #delete last item
print(f'after delete the last item: {person}')

del person['last_name']
print(f'after delete an item: {person}\n')

print(f'before changing dictionary into list: {type(person)}')
person_list = [person.items()]
print(f'after changing dictionary into tuple: {type(person_list)}\n')

person["address"].clear()
print(f'clear the dictionary: {person}')

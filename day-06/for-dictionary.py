person = {
        'first_name': 'Robertus',
        'last_name': 'Chris',
        'age': 69,
        'address': {
            'street': 'woaw',
            'zipcode': 'who cares'
            }
        }

for key in person:
    print(f'only key in dictionary: {key}\n')

for key, value in person.items():
    print(f'key and value in dictionary: {key, value}\n')

for key, value in person['address'].items():
    print(f'key and value in address dictionary: {key, value}\n')

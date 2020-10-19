dct = {
        'first_name': 'Robertus',
        'last_name': 'Chris',
        'address': {
            'street': 'nope',
            'zipcode': 'still nope'
            }
        }

dict_values = dct.values()
address_values = dct['address'].values()

print(f'personal dictionary values: {dict_values}')
print(f'address dictionary values: {address_values}')

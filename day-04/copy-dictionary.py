dct = {
        'first_name': 'Robertus',
        'last_name': 'Chris',
        'address': {
            'street': 'still tutorial',
            'zipcode': 'not gonna write it'
            }
        }

dct_copy = dct['address'].copy()

print(f'original dictionary: {dct}')
print(f'copy of dictionary address: {dct_copy}')

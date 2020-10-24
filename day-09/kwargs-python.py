def packing_person_info(**kwargs):
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')

    return kwargs

print(packing_person_info(name='Robertus', country='indo', city='surabaya', age='69'))

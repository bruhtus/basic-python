def unpack_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'

dct = {'name': 'Robertus', 'country': 'indo', 'city': 'surabaya', 'age': 69}
print(unpack_person_info(**dct))

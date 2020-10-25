import json

#python dictionary
person = {
        'name': 'Robertus',
        'country': 'indonesia',
        'city': 'surabaya',
        'skills': ['python', 'adobe lightroom', 'adobe photoshop']
        }

#convert to json
person_json_indent2 = json.dumps(person, indent=2) #indent could be 2, 4, 8. it can beautifies the json.
person_json_indent4 = json.dumps(person, indent=4) #indent could be 2, 4, 8. it can beautifies the json.
person_json_indent8 = json.dumps(person, indent=8) #indent could be 2, 4, 8. it can beautifies the json.
person_json_indent12 = json.dumps(person, indent=12) #indent could be 2, 4, 8. it can beautifies the json.
print(type(person_json_indent2))
print(f'with indent 2: {person_json_indent2}')
print(f'with indent 4: {person_json_indent4}')
print(f'with indent 8: {person_json_indent8}')
print(f'with indent 12: {person_json_indent12}')

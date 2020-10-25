import json

person = {
        'name': 'Robertus',
        'country': 'indonesia',
        'skills': ['python', 'adobe lightroom', 'adobe photoshop']
        }

with open('./json-example.json', 'a+') as f:
    json.dump(person, f, ensure_ascii=False, indent=12)

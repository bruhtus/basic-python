import json

#JSON
person_json = '''{
        "name": "Robertus",
        "country": "indonesia",
        "city": "surabaya",
        "skills": ["python", "adobe lightroom", "adobe photoshop"]
        }'''

person_dct = json.loads(person_json)
print(person_dct)
print(person_dct['skills'])

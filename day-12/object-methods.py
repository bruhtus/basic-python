class person:
    def __init__(self, firstname, lastname, gender, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        if self.gender == 'male':
            return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

        elif self.gender == 'female':
            return f'{self.firstname} {self.lastname} is {self.age} years old. She lives in {self.city}, {self.country}'


p = person('Robertus', 'Chris', 'male', 69, 'indonesia', 'surabaya')
print(p.person_info())

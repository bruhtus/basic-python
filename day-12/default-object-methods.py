class person:
    def __init__(self, firstname='Robertus', lastname='Chris', gender=None, age=69, country='indonesia', city='surabaya'):
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

        elif self.gender == None:
            return f'{self.firstname} {self.lastname} is {self.age} years old. That person lives in {self.city}, {self.country}'


p1 = person()
print(p1.person_info())

p2 = person('Robertus', 'Chris', 'male', 69, 'indonesia', 'surabaya')
print(p2.person_info())

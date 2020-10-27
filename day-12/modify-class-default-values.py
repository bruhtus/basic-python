class person:
    def __init__(self, firstname='Robertus', lastname='Chris', gender=None, age=69, country='indonesia', city='surabaya'):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        if self.gender == 'male':
            return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

        elif self.gender == 'female':
            return f'{self.firstname} {self.lastname} is {self.age} years old. She lives in {self.city}, {self.country}'

        elif self.gender == None:
            return f'{self.firstname} {self.lastname} is {self.age} years old. That person lives in {self.city}, {self.country}'

    def add_skill(self, skill):
        self.skills.append(skill)


p1 = person()
print(p1.person_info())

p1.add_skill('python')
p1.add_skill('adobe lightroom')
p1.add_skill('adobe photoshop')

p2 = person('Robertus', 'Chris', 'male', 69, 'indonesia', 'surabaya')
print(p2.person_info())

print(f'default value in class: {p2.skills}')
print(f'modify default value in class: {p1.skills}')

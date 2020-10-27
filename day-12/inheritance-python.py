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

        else:
            return f'{self.firstname} {self.lastname} is {self.age} years old. That person lives in {self.city}, {self.country}'

    def add_skill(self, skill):
        self.skills.append(skill)

class student(person):
    pass

s1 = student()
s2 = student('Anu', 'Itu', 'female', 69, 'japan', 'tokyo') #all arguments need to have value.

print(f'default values from parent class in student 1 info:\n{s1.person_info()}')
s1.add_skill('python')
s1.add_skill('adobe lightroom')
s1.add_skill('adobe photoshop')
print(f'student 1 skills: {s1.skills}\n')

print(f'modify default values from parent class in student 2 info:\n{s2.person_info()}')
s2.add_skill('what')
s2.add_skill('should')
s2.add_skill('i write')
print(f'student 2 skills: {s2.skills}')

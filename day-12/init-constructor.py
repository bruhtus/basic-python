class person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p = person('Robertus', 'Chris', 69 , 'indonesia', 'surabaya') #the order must be like the __init__ constructor
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

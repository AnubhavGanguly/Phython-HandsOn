# class Person:

#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city

#     def introduce(self):
#         print(f"My name is {self.name}")
#         print(f"I am {self.age} years old")

# person1 = Person("Anubhav", 25, "Kolkata")

# person1.introduce()

# class employee:

#     company = "ABC Company"

#     def __init__(self,name):
#         self.name = name

#     def changeCompany(self,change_company):
#         self.company = change_company

# employee1 = employee("Anubhav")

# employee1.changeCompany("XYZ Company")

# print(employee1.company)

class employee:

    company = "ABC Company"

    def __init__(self,name):
        self.name = name

    @classmethod
    def changeCompany(cls,change_company):
        cls.company = change_company

print(employee.company)
employee.changeCompany("XYZ Company")
print(employee.company)
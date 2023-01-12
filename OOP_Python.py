def parlindrome(str):
    non = False
    return str == str[::-1]


class Student:
    improve_rate = 1.05

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def age_student(self):
        print(self.age)

    def function1(self, n):
        self.age *= n


print(parlindrome('noa'))

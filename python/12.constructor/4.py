class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

name = input("Enter name: ")
age = int(input("Enter age: "))
p = Person(name, age)
p.show()

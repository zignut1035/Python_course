#! /usr/bin/python3

class MyClassWithInit:
    def __init__(self,x):
        self.x = x
object1 = MyClassWithInit(10)
print(object1.x)

class MyBadClass:
    def __init__(totally_random_name,x):
        totally_random_name.x = x
bad_object = MyBadClass(1)
print(bad_object.x)

class Zoo:
    def __init__(self, species, age, name):
        self.species = species
        self.age = age
        self.name = name
        self.zoo_name = "korkeasaari"
    def change_name(self, new_name):
        self.name = new_name
        print(self.name)
    def print_all_data(self):
        print(f"Species of the animal is {self.species}")
        print(f"Age of the animal is {self.age}")
        print(f"Name of the animal is {self.name}")

lion1 = Zoo("lion", 10, "mufaza")
lion1.print_all_data()
print(lion1.age)
print(lion1.name)
lion1.change_name('myfasa')
print(lion1.name)
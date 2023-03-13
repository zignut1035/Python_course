#! /usr/bin/python3

tuple_of_values = (1,2,3,4,5)

one, two, three, four, five = tuple_of_values

print(one)
print(two)
print(three)
print(four)
print(five)
#Does not work
#one, two, three, four = tuple_of_values

one, two, three, *rest = tuple_of_values
print(one)
print(two)
print(three)
print(rest) #[4,5]
# * in function definition
def show_cities(*args):
    print(f"what is the type of this *args thing: {type(args)}")
    for city in args:
        print(city)
show_cities("rome", "paris")

def show_cities_2(first_city, *args):
    print(f"what is the type of this *args thing: {type(args)}")
    print(f"the first city is: {first_city}")
    for city in args:
        print(city)
show_cities_2("rome","paris","pori")

dict1 = {1:"v1",2:"v2",3:"v3"}
dict2 = {4:"v4",5:"v5",6:"v6"}
#does not work
#dict3 = dict1 + dict2
dict3 = {**dict1,**dict2}
print(dict3)
dict4 = dict1
print(dict1 is dict4)#true
dict5 = {**dict1}
dict5 = dict1
print(dict1 is dict5)#false

def average_house_value(**kwargs):
    print(f"The type of kwargs is: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"key:{key}, value:{value}")
average_house_value(pori=100_000,
                    turku=200_000,
                    helsinki=400_000)
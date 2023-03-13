#! /usr/bin/python3

some_dict = {1:"value3",2:"value2",3:"value1",1:"value1"}
print(some_dict)

#for item in some_dict.item():
    #print(item)
    #print(type(item))

for key, value in some_dict.items():
    print(f"key: {key}, type {type(key)}")
    print(f"value: {value}, type {type(value)}")

for key in some_dict.keys():
    print(f"key: {key} type {type(key)}")

keys = some_dict.keys()
print(keys)
key_list = list(keys)
print(key_list[0])

for value in some_dict.values():
    print(value)
values = tuple(some_dict.values())
print(values[0])




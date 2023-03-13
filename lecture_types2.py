#! /usr/bin/python3

import numpy as np

x = np.array([1,], dtype=np.uint8)

x[0] = 1
print(x)

x[0] = 400
print(x[0])

print(bin(400))
print(bin(144))

x[0] = -1
print(x[0])
print(bin(x[0]))
y = np.array([1,], dtype=np.int8)
y[0] = -127
print(y[0])

y[0] = -128
print(y[0])

y[0] = -129
print(y[0])

first_dict = {"key":"value"}
print(first_dict)

second_dict = {"name":"johan","age":24,"is a live":True}
print(second_dict)

print(second_dict["name"])

second_dict["height"] = 175
print(second_dict)

second_dict.update(first_dict)
print(second_dict)
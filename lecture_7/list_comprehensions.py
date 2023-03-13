#! /usr/bin/python3

#new_list = [expression for member in iterable]

new_list = [x**2 for x in range(100)]

new_list2 = [x for x in range(100) if x%3 == 0]

new_list3 = [x if x%3 == 0 else "x" for x in range(100)]

new_list4 = [x for x in range(100) if 88>x>22 and x%3 == 0]
print(new_list4)

mod_list1 = [x**3 for x in new_list]

mod_list2 = [(x,x**2,x**3) for x in new_list]

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
flat_list = [x for sublist in [list1,list2,list3] for x in sublist]
#! /usr/bin/python3

def while_true():
    while True:
        print('forever')
#while_true()

def while_counter():
    counter = 0
    while True:
        counter = counter + 1
        print("not forever anymore!")
        if counter > 10:
            break

#while_counter()

def while_input():
    while True:
        answer_from_user = input('if you want to end type: end ')
        if answer_from_user == 'end':
            break
        else:
            print('so you want to keep going!')

#while_input()

def while_condition ():
    counter = 0
    while counter < 10:
        counter += 1
        print("not forever anymore!")
#while_condition()

def while_input_condition():
    answer_from_user = ''
    while answer_from_user != 'end':
        answer_from_user = input('if you want to end type: end ')
while_input_condition()        
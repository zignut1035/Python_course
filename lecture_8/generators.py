#! /usr/bin/python3

def numbers_for_ever():
    next_number = 0
    while True:
        yield next_number
        next_number += 1
print(numbers_for_ever())

generator_numbers_for_ever = numbers_for_ever()

print(next(generator_numbers_for_ever))
print(next(generator_numbers_for_ever))
print(next(generator_numbers_for_ever))

#for i in generator_numbers_for_ever:
 #   print(i, end=" ")
generator_numbers_for_ever.close()
#print(next(generator_numbers_for_ever))

generator_numbers_for_ever = numbers_for_ever()
print(next(generator_numbers_for_ever))

def yield_something_for_limited_times():
    yield "first_string"
    yield "second_string"
    yield "third_string"
    yield "fourth_string"
string_gen = yield_something_for_limited_times()
print(next(string_gen))
print("------")
def repeating_sequences():
    while True:
        yield "first thing"
        yield "second thing"
repeating_generator = repeating_sequences()
print(next(repeating_generator))
print(next(repeating_generator))
print(next(repeating_generator))
print(next(repeating_generator))
print(next(repeating_generator))

def numbers_for_ever_with_arg(num):
    next_number = 0
    while True:
        yield next_number + num
        next_number += 1
generator_for_ever_with_arg = numbers_for_ever_with_arg(0)
print(next(generator_for_ever_with_arg))
print(next(generator_for_ever_with_arg))
print(next(generator_for_ever_with_arg))
print(next(generator_for_ever_with_arg))

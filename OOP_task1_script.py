from OOP_task1_class import *

fizz = int(input('What number would you like to replace multiples of with "Fizz"? '))
buzz = int(input('What number would you like to replace multiples of with "Buzz"? '))
range_start = int(input('Where would you like to start? '))
range_end = int(input('Where would you like to end? '))

if 0 not in (range_start, range_end, fizz, buzz):
    object = test_of_multiples(range_start, range_end, fizz, buzz)
    print(object.fizzbuzz())
else:
    print('0 is not appropriate please try another input.')

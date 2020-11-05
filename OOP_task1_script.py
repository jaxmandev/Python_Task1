from OOP_task1_class import test_of_multiples

fizz = int(input('What number would you like to replace multiples of with "Fizz"?'))
buzz = int(input('What number would you like to replace multiples of with "Buzz"?'))
range_start = int(input('Where would you like to start?'))
range_end = int(input('Where would you like to end?'))

if 0 not in (range_start, range_end, fizz, buzz):
    object = test_of_multiples(fizz, buzz, range_start, range_end)
    print(object.fizzbuzz())
else:
    print('0 cannot be in the range of start, end nor can it be Fizz or Buzz, please try another input.')

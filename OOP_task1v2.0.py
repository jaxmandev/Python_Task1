min_range = int(input("Pick the an integer to start the range within which we will check for multiples.\n "))
max_range = int(input("Pick the an integer to end the range.\n "))
x1 = int(input("Pick an integer and all its multiples will turn to 'Fizz'!\n "))
x2 = int(input("Pick an integer and all its multiples will turn to 'Buzz'!\n "))
print(f"!!WARNING!! \n If a number in the range {min_range} - {max_range} is a multiple of both {x1} and {x2} it will turn to 'FizzBuzz'!\n ")

list = []
for i in range(min_range, max_range):
    if i % x1 == 0 and i % x2 == 0:
        list.append("FizzBuzz")
    elif i % x1 == 0:
        list.append("Fizz")
    elif i % x2 == 0:
        list.append("Buzz")
    else:
        list.append(i)

print(list)

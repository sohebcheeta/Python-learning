numbers = [4, 9, 12, 17, 21, 25, 30, 11]

for number in numbers:
    if number % 3 == 0:
        print(number)


numbers = [5, 12, 18, 23, 30, 41, 48, 55]

for number in numbers:
    if number > 20 and number % 3 == 0:
        print(number)


numbers = [7, 10, 15, 22, 28, 33, 40, 45]

for number in numbers:
    if (number > 20 and number % 2 == 0) or number == 15:
        print(number)

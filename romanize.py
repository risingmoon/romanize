#! /bin/env python3


# step: determine numbers
# example: 3999
# -> 3000
# -> 900
# -> 90
# -> 9

# step: determine digit and place:
# -> 3, 1000
# -> 9, 100
# -> 9, 10
# -> 9, 1

# step: exceptions:
# 4, 5, 9

chars = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'V',
    100: 'C',
    500: 'D',
    1000: 'M'
}


def romanize(num):
    text = ''
    for index, value_string in enumerate(str(num)):
        unit = 10 ** (3 - index)
        value = int(value_string)
        if value > 0 and value < 4:
            print('Less than 4')
            print(chars[unit] * value)
        elif value == 4:
            print('Four')
            print(chars[unit] + chars[unit * 5])
        elif value == 5:
            print('Five')
            print(chars[unit * 5])
        elif value > 5 and value < 9:
            print('Less than 9')
            print(chars[unit * 5] + chars[unit] * value)
        elif value == 9:
            print('Nine')
            print(chars[unit] + chars[unit * 10])


romanize(3945)

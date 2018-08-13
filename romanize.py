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
    for index, value in enumerate(str(num)):
        unit = 10 ** (3 - index)
        print(unit, value)


romanize(3000)

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
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}


def romanize(num):
    text = ''
    num_string = str(num)
    length = len(num_string) - 1
    for index, value_string in enumerate(num_string):
        unit = 10 ** (length - index)
        value = int(value_string)
        if value > 0 and value < 4:
            text += (chars[unit] * value)
        elif value == 4:
            text += (chars[unit] + chars[unit * 5])
        elif value == 5:
            text += (chars[unit * 5])
        elif value > 5 and value < 9:
            text += (chars[unit * 5] + chars[unit] * (value - 5))
        elif value == 9:
            text += (chars[unit] + chars[unit * 10])
    return text

def factorial(number, total=0):
    total += number
    if number > 1:
        total = factorial(number-1,total)
    return total

import pdb
pdb.set_trace()
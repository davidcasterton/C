#!/usr/bin/env python
"""
module: Find continuous sub-list within list with largest sum.
"""


def continuous(input_list):
    output_list = []
    max_sum = 0  # sum of max sub-list within output_list
    index_for_max = 0  # index into output_list where sum from left equals max_sum

    for item in input_list:
        output_list.append(item)

        # check for new max sub-list
        if sum(output_list) > max_sum:
            max_sum = sum(output_list)
            index_for_max = len(output_list)

        # check if current element is greater than list max
        if max_sum < item:
            output_list = [item]

    return output_list[:index_for_max]


# test
input_list = [1, 2, -8, 5, 6, -10, 7, 8, -15, 3, 4, -20, 15]
output = continuous(input_list)
print("input: %s\noutput: %s" % (input_list, output))
assert sum(output) == 16
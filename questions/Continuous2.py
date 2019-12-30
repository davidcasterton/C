
def continuous(input_list):
    if not input_list:
        # handle empty list
        return 0

    output = 0
    current = 0
    for elem in input_list:
        if elem > current + elem:
            current = elem
        else:
            current += elem

        if current > output:
            output = current

    return output


# test
input_list = [1, 2, -8, 5, 6, -10, 7, 8, -15, 3, 4, -20, 15]
output = continuous(input_list)
print("input: %s\noutput: %s" % (input_list, output))
assert output == 16


class
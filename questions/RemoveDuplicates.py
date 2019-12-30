import pdb

def RemoveDuplicates(my_list):
    #check input
    if type(my_list) != list:
        return 0
    if len(my_list) == 0:
        return 0
    #convert list to dict
    my_dict = {}
    for element in my_list:
        try:
            my_dict[element] += 1
        except:
            my_dict[element] = 1
    # return unique elements from keys of dict
    keys = list( my_dict.keys() )
    pdb.set_trace()
    print(keys)
    return keys

assert RemoveDuplicates([1,1,1,2,3,4,5]) == [1,2,3,4,5]
assert RemoveDuplicates([1,1,1,2,3,4,5,999]) == [1,2,3,4,5,999]
assert RemoveDuplicates([1,1,1,2,3,4,5,999,5626,56374568,68567]) == [1,2,3,4,5,999,5626,68567,56374568]
assert RemoveDuplicates([]) == 0
assert RemoveDuplicates({1:1}) == 0
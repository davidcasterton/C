def median( my_list ):
    import math

    unique_list = list(set( my_list ))
    num_unique = len(unique_list)
    if num_unique%2 == 0:
        print("cannot find median of list with even number of unique elements. list len: %s"%num_unique)
        return 0
    else:
        middle = math.floor( num_unique/2 )
        return unique_list[ middle ]



assert median([1,1,1,5,9,9,9,9])==5
assert median([1,2,3,4,5,6,7,8,9])==5
assert median([1,2,3,4,5,6,7,8])==0
assert median([1,1,1,1,3,5])==3
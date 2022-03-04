#26.Check circularly identical two lists
list1 = [1, 1, 1, 0, 0]
list2 = [1, 1, 0, 0, 1]
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))


'''def isCircular(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    str1 = ' '.join(map(str, arr1))
    str2 = ' '.join(map(str, arr2))
    if len(str1) != len(str2):
        return False

    return str1 in str2 + ' ' + str2'''

#12.Remove specified index from list and print
test_list = [5, 6, 3, 7, 8, 1, 2, 10]

# printing original list
print("The original list is : " + str(test_list))

# initializing idx list
idx_list = [2, 4, 5, 7]

res = []
for idx, ele in enumerate(test_list):

    # checking if element not present in index list
    if idx not in idx_list:
        res.append(ele)

# printing results
print("Filtered List after removal : " + str(res))
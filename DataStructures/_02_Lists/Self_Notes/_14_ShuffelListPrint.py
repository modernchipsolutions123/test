#15.Shuffel list and print
import random
number_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
print("Original list : ", number_list)
random.shuffle(number_list)  # shuffle method
print("List after first shuffle  : ", number_list)
random.shuffle(number_list)
print("List after second shuffle : ", number_list)

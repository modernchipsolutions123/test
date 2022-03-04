class Swapping_first_last:
    def __init__(self):
        pass
    def swap(string):
        # storing the first character
        start = string[0]
        # storing the last character
        end = string[-1]
        swapped_string = end + string[1:-1] + start
        print(swapped_string)
    swap("java")
    swap("Python")


swap1 = Swapping_first_last()
swap1.swap()

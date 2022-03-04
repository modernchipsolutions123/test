#1Check given nbr is pallindrome or Not
#Without using functions
#1.Take input from the user as string
s = input("Enter the string:")
#2.Reverse the given string
reverse = s[::-1]
print(reverse)
def pallindrome(s):
    #3.Check the string is pallindrome or not
    if s == reverse:
        print("given string is pallindrome")
    else:
        print("Given string is not Pallindrome")
pallindrome(s)



'''nbr = 121
rev = nbr[::-1]
print(rev)
if nbr == rev:
    print("Given number is pallindrome")
else:
    print("Given number is not pallindrome")




def isPalindrome(s):
    return s == s[::-1]

# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")


# function to check string is
# palindrome or not
def isPalindrome(s):
    # Using predefined function to
    # reverse to string print(s)
    rev = ''.join(reversed(s))

    # Checking if both string are
    # equal or not
    if (s == rev):
        return True
    return False


# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No") 
    '''

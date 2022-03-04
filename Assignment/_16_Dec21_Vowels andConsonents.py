'''
1.Player A and Player B playing a game and both players have same string and
 both have to make same substring using letters of string.
  player A has to make words starting with vowels(a,e,i,o,u)
 Player B has to make words starting with consonents(Without vowels)
 Count total no.of substrings.If count any nbr is greater than announce is a winner'''
'''
#1.Take input from the user as string
str1 = input("Enter the String:")
#2.Take two players
player1 = []  #2.1 Player1 has vowels aeiouAEIOU
vowels = "aAEeIiOoUu"
player2 = []  #2.2 Player2 has consonents
count = 0
#3.Iterrate the given string to vowels
for vowels in str1:
    if vowels in "AEIOUaeiou":
       print("Vowels of given string is:",vowels)'''



#1. Python program to print vowels in a string
# 1.take input from the user as string
str1 = input('Enter any string: ')
#2.Take two players player1, player2
player1 = []
player2 = []
vowels = "AEIOUaeiou"
consonents = []
#consonents = str1.replace(vowels)
#print("Consonents",consonents)
def printVowels(str1):
    # to print the vowels in str1
    for vowels in str1:
        #Check the condition of vowels
        if vowels in "AEIOUaeiou":
            print("Vowels in string1:",vowels)
            #3.Adding vowels to player1 by using append
            player1.append(vowels)
            print("Adding all the vowels in player1:",player1)
        else:
            #4.Adding consinents to player2 by using append
            player2.append(vowels)

# calling function
printVowels(str1)
print("Adding Consonents to player2:", player2)








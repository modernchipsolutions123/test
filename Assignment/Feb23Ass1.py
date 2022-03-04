str = input("Enter the string:")
wrd = str[::-1].split()
#print(wrd)
wrd = list(reversed(wrd))
print(" ".join(wrd))


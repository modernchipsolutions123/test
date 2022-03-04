str1 = "Sai Ganesh Kadali"
s1 = {str1.lower() for i in str1}
print(s1)
s1 ={str1.capitalize() for i in str1}
print(s1)

words = {'hi', 'cat', 'had', 'hat', 'in', 'one', 'trees', 'two'}
unique_words = {word.capitalize() if word[0] == 'h' else word for word in words}
print(unique_words)

str2 = {'Dance','Music','movies','Kabadi','mass'}
b = {word for word in str2 if len(word) <= 5}
print("Print 5letters of word:",b)


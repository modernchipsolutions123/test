#44.Print index character of string
word = 'Python is scripting language'
# returns first occurrence of Substringgit
result = word.find('Python')
print("Substring 'Python' found at index:", result)

result = word.find('scripting')
print("Substring 'scripting' found at index:", result)

result = word.find('of')
print("Substring 'of' found at index:",result)
# How to use find()
if (word.find('scripting') != -1):
    print("Contains given substring ")
else:
    print("Doesn't contains given substring")

txt = "Hello, welcome to my world."
print(txt.find("q")) #q is not there in given string
print(txt.index("q"))



#Dictionary Comprehension By using if condition
original_dict = {'jack':38,'michael':48,'guido':57,'john':33}
new_dict = {k:v for (k,v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict)

#By using if-else
new_dict1 = {k:('old' if v > 40 else 'young') for (k,v) in original_dict.items() }
print(new_dict1)
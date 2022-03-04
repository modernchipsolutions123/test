try:
  print(x)
except:
  print("An exception occurred")
#Try: Try block is executed when the eroor os not found
try:
  x = input("Enter the nbr x: ")
  if x == "Sai":

    print(x)
    print("Name is :",y)
  else:
    ("x is not equal to sai")
#Except: Exception block is used to rectify errors only from try block

except NameError:
  print("Variable y is not defined")
except:
  print("Something else went wrong")
#Finally: finally block is always executed.it will not depands on any block
finally:
  print("Finall block is executed")


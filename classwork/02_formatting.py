"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
correct_password = "Safestpassword321"
password = input("type password: ")
if correct_password == password:
    print("continue")
else:
    print("try again")
#i used a simple if else statement oms

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
string = input("enter a string: ")
if string == "":
    print("invalid")
else:
    print("valid")
#another if else statement being used 

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
animal = "dog"
new_animal = animal.replace('dog' ,'cat')
print(new_animal)
#copied and pasted from the slides and just removed and replaced words

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
name = "Bartholmew"
age = 72
print(f"My name is {name} and I am {age} years old.")
#thank you god for opening tasks
"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""

#idk the beginning part </3 :'(
print("The value is {0:.2f}".format(3.14159))
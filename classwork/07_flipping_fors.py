"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
     print(fruits)
#just printing my list using the for loop
"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
numbers = ["1", "11", "111"]
sum = 0
for number in numbers:
     sum += number
print (f"the sum of the numbers in the list is: {sum}")
#made a list used the for loop used a part of the list from the entire thing for the addition portion of the code. 
"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
n = "Hello I need help with my Pre-Calc homework"
print(len(n))

#used len function in my print function and got my length
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result
"""
dictionary = {
     "name": "Noel",  
     "age": 17,
     "school": "bghs",
     "emotion": "RELEASE MEEEEE"
}
for key, value in dictionary.items():
    print(f"{key}: {value}")
#used dictionary to store my data and printed it using "for key" loop and got my values printed in the terminal
"""
In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
#yes all of it was expected
"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
for x in range(1, 11):
    print(x)
#used range funtion and for loop ong
"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
for x in range (900, 1001, 10):
    print(x)
#same thing from task 1 
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
for x in range (1, 101, 9):
    print(x)
#same thing from task 1 and 2 
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for number in numbers:
     sum += number
#actually got this from previous topic questons to find the sum function and worked from there.
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?
"""
#* 
#* 
#* 
#* 
#* 
#* 
#* 
#* 
#* 
#* 
#* 
#* 
#* 
#* 
#* 
"""
- Explain the iterative process that this code executes to get that output
"""
#uses the print function and prints 'x', and end=" " and gives said output 
rows = 5

for i in range(rows):
     for j in range(i + 1):
       print('*', end=' ')
       print()
"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""
def my_function(name): 
    print("Hello " + name)

my_function("Bob")
#copied str8 frm the slides B)
"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def squared_num(i):
    return i ** 2

vanderbilt = squared_num(42)

#squaring 42 on gang B)
"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
number = int(input("enter a number: "))
def TruOrFal (num):
    if num % 2 <= 0:
        return num, "is even."
    else:
        return num, "is odd."
HEEELppppp = TruOrFal(number)
#if else statement to a true or false statement to determine if the number is even or odd
"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
def multiply_num(a, b): 
    return a * b

x = multiply_num(7, 8)
"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""


"""
Task 6: Average of Numbers
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, and returns the total.
Your function should also optionally accept a 3rd argument for discount, and return the discounted if provided.
"""
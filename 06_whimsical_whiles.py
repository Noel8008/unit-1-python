"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
i = 1

while i < 11:
    print(i)    
    i += 1

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
n = 10

while n > 0:
    print(n)
    n -= 1
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
def factorial(n):
    if n < 0:
        return("factorial not in negative numbers")
    answer = 1 
    count = 1
    while count <= n:
        answer *= count
        count += 1
    return answer

number = int(input("enter a number"))
print(f"the factorial of {number} is {factorial(number)}")
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""


"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""
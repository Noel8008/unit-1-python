#2
print("give me a number")
num = int(input())

for num in range(1, num):
    if num % 2 <= 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")
#range function had to fix the if statement and put the proper variables.

#3
num = int(input("Enter an integer: "))

if num < -1:
  print("No negative numbers.")
else:
  result = 1
  for i in range(1, num):
    result *= i   

  print("Factorial of " + num + "is" + result)

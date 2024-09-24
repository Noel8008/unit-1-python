"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
a=17.38
b=int(a) #converting my float into an interger using the int function on my soul
print(a)
print(b)

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
number= int(input("input any letter of the numberline"))
if number >0:
    print("Its Positive!!!!")
elif number==0:
    print("oms its a zero")
else: 
    print("its a negative") #made a if, elif, else statements to see any number you type would give you the "value" of said typed number

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
i=input("input a whole number")
f=input("input a decimal number")
print(i+f)
print(i-f)
print(i*f)
print(i/f)
#making the answer show up in the print after putting all math operations
"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
store ={
   "apples": 7,
   "bananas": 8,
   "oranges": 6
}

pasting = store["oranges"]
print(str(pasting))


"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
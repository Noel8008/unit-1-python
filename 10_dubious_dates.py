"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
from datetime import datetime 
my_dt = datetime.now()
print(my_dt)

#use the now function get the exact date and time
"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
from datetime import date
my_date = date.today()
my_string = my_date.strftime("%m/%d/%Y")
print(my_string)
#slides helped me with this one but got the date imported from the module datetime made my variable meanings and made the date format and executed from there 
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
from datetime import datetime
date_1 = 
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
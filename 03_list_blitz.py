"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""

elements = ["fire", "water", "earth", "air"]
print(elements)

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""

elements.append("electricity")
print(elements)
#using the append function

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""

del elements [2]
print("elements")
#using del function 

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

elements [3]= "aang"
print(elements)
#oms used indexes

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
new_elements = ("electrictiy")
elements.append("new_elements")
print(elements)


"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""

del elements [0]
print(elements)

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""

updated_elements = elements[0:2]
print(elements)

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

element_a = ["fire", "water", "earth", "air"]
element_b = ["electricity, space,"]
the_avatar = element_a + element_b
print (the_avatar)
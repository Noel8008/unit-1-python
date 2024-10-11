"""
task 0: class we do 
"""
class Character:
    health = 100

    def __init__(self, name):
        self.name = name

    def damage(self, dmg=12):
        self.health = self.health - dmg

    def heal(self):
       if self.health < 100:
        self.health = self.health + 10
    
class player(Character):
   health = 50

enemy1 = Character("Xx024N00b_Master420xX")
enemy1.damage()
print(enemy1.health)

player1 = player("DoughBoy")
player1.damage(5)
player1.heal()
print(player1.health)
"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class Person:
   species = 'Homosapien'
    
    def __init__(self, name, age): #the classes for its name and age
        self.name = name 
        self.age = age

    def introduction(self): #the introduction of Jack
        return f"top of the morning my name is {self.name} and I am {self.age} years old"

human = Person("Jack", 32)

introduction = human.introduction()
print (introduction)


"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
class Animal:
   def speak(self): #empty method called speak 
      
    class Dog:
        def speak(Animal):
           return "bark"
           
        class Cat(Animal):
           def speak(Animal):
              return "cat"

"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
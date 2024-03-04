#############################
# Question 1: Class Bicycle #
#############################

class Bicycle:
    def __init__(self, model, color, price, stock = 0):
        self._color = color # The underscore is to indicate that the attribute is private (it is not necessary)
        self._model = model
        self._price = price
        self._stock = stock
    
    # Question 2: Accessories
        
    def __repr__(self) -> str:
        return f"{self._model} ({self._color}) - ${self._price} - {self._stock} in stock"
    
    def get_model(self):
        return self._model
    
    def get_color(self):
        return self._color
    
    def get_price(self):
        return self._price
    
    def get_curr_stock(self):
        return self._stock
    
    # Question 2: Mutators
    
    def set_model(self, model):
        self._model = model
    
    def set_color(self, color):
        self._color = color
        
    def set_price(self, price):
        self._price = price
        
    def set_stock(self, stock):
        self._stock = stock
    
    def increase_stock(self, n):
        self._stock += n
    
    def decrease_stock(self, n):
        self._stock -= n


# bike1 = Bicycle("Mountain111", "Red", 300)
# bike2 = Bicycle("City200", "Blue", 300)

# print(bike1)
# print(bike2)

# bike1.increase_stock(10)

# print(bike1.get_curr_stock())


#################################
# Question 3: Class BankAccount #
#################################

class BankAccount:
    def __init__(self, acct_no, balance):
        self._acct_no = acct_no
        self._balance = balance
        
    def __repr__(self) -> str:
        return f"Account No: {self._acct_no} - Balance: ${self._balance}"
    
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount
            
    def deposit(self, amount):
        self._balance += amount
        
# bankAccount1 = BankAccount(123, 1000)

# print(bankAccount1)

#################################################
# Question 4: Person, Student and Teacher Class #
#################################################

class Person:
    def __init__ (self, name, gender, age):
        self._name = name
        self._gender = gender
        self._age = age
        
    def __repr__(self) -> str:
        return f"Name: {self._name} - Gender: {self._gender} - Age: {self._age}"
    
class Student(Person):
    def __init__(self, name, gender, age, classGroup):
        super().__init__(name, gender, age)
        self._classGroup = classGroup
        
    def __repr__(self) -> str:
        return super().__repr__() + f" - Class: {self._classGroup}"

class Teacher(Person):
    def __init__(self, name, gender, age, subject):
        super().__init__(name, gender, age)
        self._subject = subject
        
    def __repr__(self) -> str:
        return super().__repr__() + f" - Subject: {self._subject}"

# person1 = Person("Yunsong", "Male", "16")

# student1 = Student("Yunsong", "Male", "16", "4A3")

# teacher1 = Teacher("Mr Zhou", "Male", "39", "Computing")

# print(person1)
# print(student1)
# print(teacher1)

#######################
# Question 5: Mammals #
#######################

class Mammal:
    def __init__(self, name):
        # Your code here
        
        self._name = name
        
    def get_name(self):
        # Your code here
        return self._name
    
    def say(self):
        # Your code here
        return f"What does the {self._name} says"
    
#####################################
# Question 6: Mammalian Inheritance #
#####################################

# You DO NOT NEED TO DEFINE Mammal class here!

class Dog(Mammal):
    def __init__(self):
        super().__init__("Dog")
 
        
# Cat definition should go here
class Cat(Mammal):
    def __init__(self):
        super().__init__("Cat")


# Fox definition should go here
class Fox(Mammal):
    def __init__(self):
        super().__init__("Fox")
        
######################################
# Question 7: Mammalian Polymorphism #
######################################

# Dog definition should go here

class Dog(Mammal):
    def __init__(self):
        super().__init__("Dog")
        
    def say(self):
        return "Woof"

# Cat definition should go here

class Cat(Mammal):
    def __init__(self):
        super().__init__("Cat")
        
    def say(self):
        return "Meow"

# Fox definition should go here

class Fox(Mammal):
    def __init__(self):
        super().__init__("Fox")
        
    def say(self):
        return "Ring-ding-ding-ding-dingeringeding"

print(Dog().say())

#################################
# Question 8: UML Class Diagram #
#################################


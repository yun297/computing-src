###################
# Drawing a shape #
###################

# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

############################
# Variables and data types #
############################

# name = "John"
# age = 10
# print("There was once a man named " + name + ".")
# print("He was " + age + " years old.")
# print("He really liked the name " + name + ",")
# print("but he didn't like being " + age + ".")

########################
# Working with strings #
########################

# phrase = "Big Balls"
# # print(phrase.replace("Big", "Small"))
# print(phrase.upper().isupper())

# print(phrase[0])

########################
# Working with numbers #
########################

from ast import Num
from math import * # Importing more math functions (Importing a math module)
from types import resolve_bases 

# print(-9.84972)
# print(3 + 4) # Addition
# print(3 - 4) # Subtraction
# print(3 * 4) # Multiplication
# print(3 / 4) # Division
# print(10 % 3) # Mod (Remainder)
# print(3 * (3 + 4)) # Complex equations

# num = 5
# print(num)
# print(str(num)) # Converting number to string
# num = str(num) # Storing it in num
# print(num + " is my favourite number.") # Connecting strings with other strings

# neg_num = -5
# print(abs(neg_num)) # Absolute

# print(pow(3, 2)) # 3 raised to the power to 2

# print(max(4, 6)) # Returns larger number

# print(min(4, 6)) # Returns smaller number

# print(round(3.2)) # Rounding to whole number

# print(floor(3.7)) # Rounds down

# print(ceil(3.7)) # Rounds up

# print(sqrt(36)) # Square root

############################
# Getting inpur from users #
############################

# user_name = input("Enter your name: ")
# user_age = input("Enter your age: ")
# print("Hello " + user_name + "! You are " + user_age + "!")

#########################
# Building a calculator #
#########################


# cal_num1 = input("Enter a number: ")
# cal_num2 = input("Enter another number: ")
# cal_result = float(cal_num1) + float(cal_num2)

# print(cal_result)

#################
# Mad Libs Game #
#################

# madlibs_color = input("Enter a color: ")
# madlibs_noun = input("Enter a plural noun: ")
# madlibs_celeb = input("Enter a celebrity: ")

# print("Roses are " + madlibs_color + ",")
# print(madlibs_noun + " are blue,")
# print("I love " + madlibs_celeb + ".")

#########
# Lists #
#########

# colors = ["Red", "Yellow", "Green", "Purple", "Orange"]

# print(colors) # Priting whole list
# print(colors[0]) # Priting a specific value in list with indexing
# print(colors[-1]) # Printing a specific value in the list using negative indexing

# print(colors[3:]) # Printing values from index 3 onwards
# print(colors[0:2]) # Priting values from index 0 to 1 (up to 2, 2 is not included)

# colors[1] = "Blue"

# print(colors[1])

##################
# List Functions #
##################

# lists_numbers = [6, 9, 4, 2, 0, 42]
# lists_colors = ["Red", "Yellow", "Green", "Purple", "Orange"]

# lists_colors.extend(lists_numbers) # Adding 2 lists together

# lists_colors.append("White") # Adding another value to the back of the list

# lists_colors.insert(1, "Black") # Inserting new value at index postion 1

# lists_colors.remove("Purple") # Removing a value from the list

# lists_colors.clear() # Clearing the list (removing everything)

# lists_colors.pop() # Removes last element on the list

# print(lists_colors.index("Red")) # Finding the index of a value in the list, if value is inexistent, an error will be returned

# print(lists_colors.count("Red")) # Checking the number of times a vlaue appears in the list

# lists_colors.sort() # Sorting in ascending order or alphabetical

# lists_colors.reverse() # Reverse the order of the list

# lists_colors2 = lists_colors.copy() # Copy one list to another

# print(lists_colors2)

##########
# Tuples #
##########

# coordinates = (4, 5) # Creating a tuple, a tuples is immutable, meaning it can't be changed. It is similar to lists, but it cannot be changed and it is created using parenthesis instead of square brackets

# print(coordinates[0])

# coordinates_list = [(1, 2), (3, 4), (5, 6)] # A list of tuples

#############
# Functions #
#############

# def say_hi(name, age): # Defining function
#     print("Hello " + name + "! You are " + age + "!")

# user_name = input("Enter your name: ")
# user_age = input("Enter your age: ")

# say_hi(user_name, user_age) # Calling the function while including parameters

###################
# Return function #
###################

# def cube(num):
#     return num*num*num # Returning a value back to the caller
#     # When the return keyword is used, it will break out of the function and won't reach the code beyond the return keyword

# result = cube(4) # Storing the returned value into the variable
# print(result)

#################
# If statements #
#################

# is_male = True
# is_tall = False

# if is_male and is_tall:
#     print("Your are a tall male")
# elif is_male and not(is_tall): # not() negates the value in the parenthesis
#     print("You are a short male")
# elif not(is_male) and is_tall: # You can stack elif(s) between if and else (nested else if)
#     print("You are not a male but are tall")
# else:
#     print("You are either not male or not tall")
    
###############################
# If statements & comparisons #
###############################

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# print(max_num(3, 4, 5))

################################
# Building a better calculator #
################################

# num1 = float(input("Enter the first number: "))
# op = input("Enter the operator(+, -, *, /): ")
# num2 = float(input("Enter the second number: "))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1 * num2)
# elif op == "/":
#     print(num1 / num2)
# else:
#     print("Invalid operater, please enter either +, -, * or /")

################
# Dictionaries #
################

# monthConverisons = { # Creating dictionary
#     "Jan": "January", # Defining key value pairs, by defining the key and give it a corresponding value
#     "Feb": "February", # Duplicate keys cannot be used
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December"
# }

# print(monthConverisons["Dec"]) # Getting the value using the corresponding key
# print(monthConverisons.get("Dec")) # Getting the value using the corresponding key with get function

# print(monthConverisons.get("asdasd", "Not a valid key")) # Using the get function can return a default value if invalid keys are used

##############
# While loop #
##############

# i = 1
# while i <= 10: # Everytime i is >= to 10 it will loop the program again
#     print(i)
#     i += 1 # Adding 1 to the i and setting i as that value

# print("Done with loop") # If the condition is no longer true, it will end the while loop and move on to the next line of code

############################
# Building a guessing game #
############################

# secret_word = "balls"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter in your guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True

# if out_of_guesses:
#     print("Out of guesses, YOU LOSE!")
# else:
#     print("YOU WIN!")

############
# For loop #
############

# friends = ["Sugon", "Dragon", "Candice"]

# for index in range(len(friends)):
#     if index == 0:
#         print("First iteration")
#     else:
#         print("Not first")
#     print(friends[index])

#####################
# Exponent function #
#####################

# print(2**3) # 2 raised to the power to 3 (exponent)

# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result

# print(raise_to_power(8, 7))

###########################
# 2D lists & nested loops #
###########################

# number_grid = [ # Lists of lists (2 dimensional array)
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]

# print(number_grid[2][1]) # Priting out 8 from the grid (row 3 which is index 2 and column 2 which is index 1)

# for row in number_grid:
#     for col in row:
#         print(col)

#########################
# Building a translator #
#########################

# Balls Language
# vowels --> g
# --------------

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"

#         else:
#             translation = translation + letter
#     return translation

# print(translate(input("Enter a phrase: ")))

############
# Comments #
############

# This is a comment
# It won't run

'''
This is also a comment
'''

# print("Comments are fun!")

################
# Try / Except #
################

# try:
#     number = int(input("Enter a number: "))
#     print (number)
# except:
#     print("Invalid input")

# For example in this program, if a user does not enter a number, it will return an error
# But since there is a try/expect block it will return the code under the except block

# However this can catch all errors

# try:
#     number = int(input("Enter a number: "))
#     print (number)
#     10 / 0
# except:
#     print("Invalid input")

# Even though a number is entered, the zero division error was caught

# try:
#     number = int(input("Enter a number: "))
#     print (number)
#     10 / 0
# except ZeroDivisionError:
#     print("Divided by 0")
# except ValueError:
#     print("Invalid input")

# Different output depending on the error

# Storing error as a variable

# try:
#     number = int(input("Enter a number: "))
#     print (number)
#     10 / 0
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid input")

#################
# Reading files #
#################

# Modes to open a file
# "r" - read (only can read the file, cannot change the file)
# "w" - write (can only write the file)
# "a" - append (can only add new info to the end of the file but cannot modify any existing info)
# "r+" - read and write (can read and write the file)

employee_file = open("employees.txt", "r") # Storing as a variable

# Always make sure to check if the file is readable

# print(employee_file.readable()) # Returns a boolean value

# print(employee_file.read()) # Reads the whole file

# print(employee_file.readline()) # Reads the first line and moves to the next line

# print(employee_file.readline()) # By using this function again, it reads the next line and so on

# print(employee_file.readlines()) # Storing each line as a value of a list

# print(employee_file.readlines()[1]) # Printing index 1 of the list

# for employee in employee_file.readlines():#
#     print(employee) # Priting each line in the file using a for loop

# Always remember to close the file

employee_file.close() # Closing using the close() function on the variable

####################
# Writing to files #
####################

# Lets say we want to add a new employer to the file

# employee_file = open("employees.txt", "a") # Appending to the file

# employee_file.write("Toby - Human Resources") # Adding a new line to the file

# Be careful not append twice or you will get 2 of the same lines

# Use \n to add a new line

# employee_file.write("\nKelly - Customer Service")

# employee_file = open("employees.txt", "w") # Writing

# employee_file.write("Kelly - Customer Service") # This will overwrite the entire file

# employee_file = open("index.html", "w") # Creating a new file if the file name is non existent, you can use other file formats

# employee_file.write("<p>This is a HTML file</p>")

###################
# Modules and Pip #
###################

# A module is a python file that we import to our current python file, usually containing useful functions, and you can access all the variables in the other file

# import useful_tools

# print(useful_tools.roll_dice(10)) # Importing roll dice function from other file

# https://docs.python.org/3/py-modindex.html

#####################
# Classes & Objects #
#####################

# A class is a custom data type, which can be made up of the base python data types

from Student import Student

# student1 = Student("Sugon", "Business", 3.1, False)
# student2 = Student("Candice", "Math", 2.5, True)

# print(student1.gpa)
# print(student2.major)

###################################
# Building a multiple choice quiz #
###################################

# from Question import Question

# question_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#     "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
# ]

# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b")
# ]

# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

# run_test(questions)

####################
# Object functions #
####################

from Studentv2 import Studentv2

# studentv2_1 = Studentv2("Oscar", "Accounting", 3.1)
# studentv2_2 = Studentv2("Phyllis", "Business", 3.8)

# print(studentv2_1.on_honor_roll())

###############
# Inheritance #
###############

from Chef import Chef
# myChef = Chef()
# myChef.make_chicken()
# myChef.make_salad()
# myChef.make_special_dish()

from ChineseChef import ChineseChef

# myChineseChef = ChineseChef()
# # myChineseChef.make_chicken()
# # myChineseChef.make_salad()
# myChineseChef.make_special_dish()
# myChineseChef.make_fried_rice()

######################
# Python Interpreter #
######################


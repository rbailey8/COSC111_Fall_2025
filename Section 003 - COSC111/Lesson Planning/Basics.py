# # Basics of printing in python

# # Python looks at the instructions in order line by line. 
# # The order in which we write the instructions matters. And it executes the
# # behavior 

# # Let's build a house
# print("    /\\")
# print("   /  \\")
# print("  /    \\")
# print(" /      \\")
# print("/        \\")
# print("----------")
# print("|  |  |  |")
# print("|  |  |  |")
# print("----------")
# print("|  |  |  |")
# print("|  |  |  |")
# print("----------")
# print("|        |")
# print("----------")

# #    Variables
# # A lot of time we are dealing with a lit of different data. 
# # And we need a way to store different data values. 
# # We can create containers that can store data for us, 
# # they are known as variables


# print("There was a student named Serena who wanted to be a software engineer.")
# print("She was passionate about computers and curious to learn about computer science.")
# print("So she attended Morgan State and majored in computer science at the age of 18.")
# print("Her first class was called COSC111.")

# # Instead of adding the name and age directly we can replace the age and name with a variable. 
# character_name = "Serena"
# age = "18"
# # When we get to the variable, the code knows we want to print the value store in the variable character_name
# print("There was a student named " + character_name +  " who wanted to be a software engineer.")
# print("She was passionate about computers and curious to learn about computer science.")
# print("So she attended Morgan State and majored in computer science at the age of " + age + ".")
# print("Her first class was called COSC111.")

# # 
# # Now if we want to change the value inside the variable, we can change it 
# character_name = "Brianna"
# print("We created a new student named " + character_name +  ".")

# # There are different types of data we can store

# # String - is essentially text but it must start and end with a single ' ' or double quote " "
# 'This is a string'
# "This is also a string"

# # Numbers - a number can be a whole number or decical number
# # This is a whole number
# age = 2
# # This is a float - in python we call decimal numbers float
# 3.5

# # Boolean - a true or false value 
# # This is a true boolean 
# boolean_1 = True
# # This is a false boolean
# boolean_2 = False


# # Input
# # We are going to get information from a user and storing the value. 
# # All we need to do is use the built in function called input(). 
# # Using the function tells the code we need to get an input from the user. 
# # We can have the user give us multiple pieces of information.

# # Enter a prompt into the user argument 
# user_name = input("Enter your name: ")
# user_age = input("How old are you: ")
# print("Hello " + user_name + ". You are " + user_age + " years old.")

# # Let's build a very basic calculator

# # Start by creating 2 variables. By default python stores the input value as a string. To convert it into a number we have to use a special function. 
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = num1 + num2
# print(result + " This result combines the strings of the numbers")

# num1 = input("Enter a number that is an integer: ")
# num2 = input("Enter another number that is an integer: ")
# result = int(num1) + int(num2)
# print(f"{result} This result adds the integers")

# num1 = input("Enter any number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# print(f"{result} This result adds the floats")

# Working with string
print("New York")
# We can add a \n which creates a new line. And prints 
# Line 1: New
# Line 2: York
print("New \n York")

# This means hey python I want to print out a quotation mark
print("\"")

# We can also print a backslash
print("\\")
print("\\")

# Concatenation - combining multiple string together
city = "Baltimore"
state = "Maryland"
print(city + " " + state)

# We can also use special things called functions that are built in and can be used
# to modify our strings and can be used to get info about the strings

# Make all character lower case
print(city.lower())
# Make all characters upper case
print(state.upper())
# Make 
print(state.isupper())

# Find the length of the string. The number of characters
print("\"cat\" has {} characters".format(len('cat')))

# Print automatically adds space between the characters
print("hi", "there")

# If we want to access a specific characters we can get the number order of the letter. 
# To get the value it is important to note, the first character is in position 0
question = "What's your name?"
print(question[0])
print(question[1])
print(question[2])
print(question[3])

# We can search for the first index of a character using the .index function on a string
phrase_1 = "COSC111 is my favorite class"
# Search for first index of O 
# Prints -> 2
print(phrase_1.index("S"))

# We can also find the index where a phrease starts
print(phrase_1.index("111"))

# If the string is not found it returns a "ValueError: substring not found"
# print(phrase_1.index("apple"))

# Anytime we put a value into a function we call that passing in a parameter. 

# Replace words or letters


# Arithmetic Operators


# Casting data operator
midterm_grade = 97
# Converts the value into it's string version
midterm_grade = str(97)
# Finds the type of the provided value
print(type(midterm_grade))

# Convert the string to an int value if possible
midterm_grade = int(midterm_grade)
print(type(midterm_grade))

# Convert a value into a float
mcdonalds_fries_cost = 5
mcdonalds_fries_cost = float(mcdonalds_fries_cost)
print(type(mcdonalds_fries_cost))

# Convert back into an integer
mcdonalds_fries_cost = int(mcdonalds_fries_cost)
print(type(mcdonalds_fries_cost))

# Casting data types is converting a value from one data type to another data type. 
# It is useful when you need to change the data tupe to meet the needs of a program

# Integer - casts to an integer value
int()
# Float 
float()
# String - cast to float
str()
#Boolean - casts to boolean 
bool()


# Integer to Boolean
x_val = 24
x = bool(x_val)
y_val = 8
y = bool(y_val)
print(f"Converting the number {x_val} to {x} boolean value")
print(f"Converting the number {y_val} to {y} boolean value")

# Cast with an input
sleep_amount = int(input("How many hours of sleep do you get daily?: "))
print(f"You sleep {sleep_amount} hours a day")

# Return Values
# Some functions return a value instead of displaying or storing values. 
# Some examples include str(), int(), float and bool() which return values but don't display them. 
tv_size = 48.21
print(f"tv size is {int(tv_size)}")


# In the above line we are passing a return value as an argument to a functon


# Lists - casts to list
list()

# Numbers
# Simple to print a number
print(2) # outputs 2 
print(2 + 5) # outputs 7

# Addition
print(100 + 20)

# Subtraction()
print(100 - 20)

# We use pemdas to handle the order operation
print((2*2) + 4) # returns 8

# Converts number tp a string
my_number = 14
print(str(my_number) + " my favoriate number")

# Modulus - takes the 1st number fivides by the second an gets the remainser
print(11%2)

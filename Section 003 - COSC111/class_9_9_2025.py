print("\nHello World\nClass starts at 1pm")

# Line 1: Blank
# Line 2: Hello World
# Line 3: Class starts at 1pm

print()
print("Hello World")
print("Class starts at 1pm")
# Line 1: Blank
# Line 2: Hello World
# Line 3: Class starts at 1pm

# The following is the same

print('I\'m taking 5 classes this \nsemester \n and I like it')
# Line 1: I'm taking 5 classes this or blank
# Line 2: semester 
# Line 3: and I like it

print("Dr.Wang says \"CS is the best major\"")
# How do we know the beginn

# Data Types

# String
netflix_password = 'safestPassword'

# Numbers

# Integers - whole number
class_size = 21
exam_score = 100
print(f"class_size: {class_size}")
print(f"exam_score: {exam_score}")

# Floats - decimals
pi = 3.14
print(f"pi = {pi}")

# Boolean
true_value = True
false_value = False
print(f"true_value = {true_value}")
print(f"false_value = {false_value}")


# Operation in numbers
result = 5 + 3.0
print(f"What is the output?: {result}")
print(f"What is the data type?: {type(result)}")

# Type as a built in function to determine the data type of a value
print(type(True))
print(type(35))
print(type("COSC111"))

# Addition 
result = 8 + 9
print(f"8 + 9 = {result}")

result += 3 # same as result = result + 3
print(f"result + 3 = {result}")




# Subtraction 
result = 15 - 5
print(f"15 - 5 = {result}")
result -= 25 # same as result = result -15
print(f"result -  25 = {result}")

# Multiplication 
result = 10 * 6
print(f"10 * 6 = {result}")
result *= 2 # same as result = result * 2
print(f"result * 2 = {result}")

# Divsion 
result = 24 / 3
print(f"24 / 3 = {result}")
result /= 2 # same as result = result /2
print(f"result / 2 = {result}")

# Floor 
result = 25 // 3
# 25 / 3 = 8 remainder 1
print(f"25 // 3 = {result}")
result //= 2 # same as result = result // 2
print(f"result // 2 = {result}")

# Modulus
result = 25 % 3
print(f"25 % 3 = {result}")
result %= 2 # same as result = result % 2
print(f"result % 2 = {result}")

# Exponent
result = 2 ** 8 # 2^8
print(f" 2**8 = {result}")


# PEMDAS - Order of operations
# Parenthesis
# Exponents
# Multiplication
# Division
# Addition
# Subtraction

result = (10 - 2) * 3 + 8 / (7-5)
#            8    * 3 + 8 / 2
#            8    * 3 + 8 / 2
#                  24 + 8 / 2
#                  24 + 4 = 28
print(result)

x = 10
y = 5
result = x + y * 2 
#       10 + 5 * 2
#       10 + 10 = 20
print(result)

a = 15
# a -= 5 * 2
a = a - 5 * 2
print(a)

result = 12/3 + 4 * (8 - 6)
#        12/3 + 4 * 2
#        12/3 + 8
#           4 + 8 = 12
print(result)

x = 2 
y = 3
result = x ** 2 + y * 5
#        2 ** 2 + 3 * 5
#             4 + 3 * 5
#             4 + 15 = 19       
print(result)

a = 25
a //= 3
# a = a // 3
#   25 // 3 = 8 

a %= 2
# 8 % 2 = 8/2 = 4 remainder 0
print(a)


result = (1 + 3) * 5
print("result")
print(result)

print(type(24))

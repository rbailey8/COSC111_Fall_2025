# Data Types
#   Float
#   Integer
#   Bool
#   String
#   List

# Casting Data Type - changing the data type of a value

# Integer to String
result = str(10)
result_type = type(result)
print(f"result str(10): {result}, type: {result_type}")

# Integer to String
result = float("1001")
result_type = type(result)
print(f"result float(\"1001\"): {result}, type: {result_type}")

# Int to Bool
result = bool(0)
result_type = type(result)
print(f"result bool(0): {result}, type: {result_type}")
result = bool(1)
result_type = type(result)
print(f"result bool(1): {result}, type: {result_type}")

age = input("Age: ")
interest = input("Interest: ")
age = int(age)
# How can we determine if someone is an adult
isAdult = age >= 18
print(f"User is {age}, are they an adult: {isAdult}")

# How can we determine if someone is an young child
isYoungChild = age <= 10
print(f"User is {age}, are they a young child: {isYoungChild}")

# Conditional Operations

# Greater than 
result = 100 > 4
print(f"100 > 4 = {result}" )

# Less than 
result = 100 < 400
print(f"100 < 400 = {result}" )

# Equals 
result = 100 == 400
print(f"100 == 400 = {result}" )

val_1 = 100
val_2 = "100"
result = val_1 == val_2
print(f"val_1 == val_2: {result}")

# Not Equal - reverse of equals
val_1 = 100
val_2 = "100"
result = val_1 != val_2
print(f"val_1 != val_2: {result}")

# Combine multiple conditional

# and

# Is the user an adult programmer (18+ and interest in programming)
isProgrammer = interest == "programming"
isAdultProgammer = isAdult and isProgrammer
print(f"isProgrammer: {isProgrammer}. isAdult: {isAdult}")
print(f"Is user an adult programmer: {isAdultProgammer}")
# When using and all conditions must be true for output to be true
# false and true and true... -> false

# or
isProgrammer = interest == "programming"
isAdultOrProgammer = isAdult or isProgrammer
print(f"isProgrammer: {isProgrammer}. isAdult: {isAdult}")
print(f"Is user an adult or a programmer: {isAdultOrProgammer}")
# true or false or false -> true

# not - reverse the result of a conditional
value1 = 1000
value2 = "1000"
# result = not(value1 == value2) # as same is !=
result = value1 is not value2
print(f"Is {value1} == {value2}: {result}")


# If Statement
hasAdultAccess = False
print()
if not isAdult:
    hasAdultAccess = True
    print("The user has adult access was changed to True")

# if conditional statement (only be True or False)
# if True and True and (True or True or False):
#     print("If statement is executed")
# if True:
#     print("If statement is executed")
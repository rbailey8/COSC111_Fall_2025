# Data Types
# - Float
# - Integer
# - String
# - Bool
# - List

# Cast Type built-in functions - convert from 1 type to another
result = "75"
result = int(result)

# Build in type function to know which data type
result_type = type(result)
print(result)
print(f"{result} has the type {result_type}")

# Convert to a float
result = float(result)
result_type = type(result)
print(f"{result} has the type {result_type}")

# Convert to a string
result = "Morgan State"
result = list(result)
result_type = type(result)
print(f"{result} has the type {result_type}")

# What is you age
age = input("Age: ")
# What is your interest
interest = input("What is your interest: ")

# Are you 18 or older
# True or False
age = int(age)
isAdult = age >= 18
print(f"Is person age {age} an adult: {isAdult}")

# Are you younger than 10
# True or False
isYoungChild = age <= 10
print(f"Is person age {age} a young child {isYoungChild}")

# Equals
result_1 = 100
result_2 = "100"
isResultEqual = result_1 == result_2
print(f"Is {result_1} equal to {result_2}: {isResultEqual}")

result_1 = 1001.0
result_2 = 1001
isEqual = result_1 == result_2
print(f"Is {result_1} equal to {result_2}: {isEqual}")

isNotEqual = result_1 != result_2
print(f"Is {result_1} equal to {result_2}: {isNotEqual}")

# Combining conditionals 

# And - combine multiple bool value 

# Is an adult and interest in programming
isProgrammer = interest == "programming"
isProgrammingAdult = isAdult and isProgrammer
print(f"isAdult: {isAdult} isProgrammer: {isProgrammer}")
print(f"Is this person an adult that programs: {isProgrammingAdult} ")

# Or
isAdultOrProgrammer = isAdult or isProgrammer
print(f"isAdult: {isAdult} isProgrammer: {isProgrammer}")
print(f"Is this person an adult or do they program: {isAdultOrProgrammer} ")

# not is the same as != 
result_1 = "soccer"
result_2 = "futbol"
result = not (result_1 == result_2)
print(f"result1: {result_1}, result_2: {result_2}. Are they not equal: {result}")
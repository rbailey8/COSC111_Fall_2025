
# Functions that convert data types
result = int("100")
print(f"int(\"100\"): {result}")

result = float("1313")
print(f"float(\"1313\"): {result}")

result = str(13)
print(f"str(13): {result}")

result = bool(0)
print(f"bool(0): {result}")

result = list("Morgan State")
print(f"list(\"Morgan State\"): {result}")

# Conditional Operators

print(f"10 > 5 {10 > 5}") # True
print(f"100 < 15 {100 < 5}") # False
val_1 = "100"
val_2 = str(100)
result = val_1 == val_2
print(f" \"100\" == str(100) {result}") #False

age = input("Age: ")
interest = input("Interest: ")
age = int(age)
# Is a user an adult
isAdult = age >= 18

# Combine Conditionals

# and - combine bool value. Only true when all values are true.

# Is person an adult that is a programmer
isProgrammer = interest == "programming"
isAdultProgrammer = isAdult and isProgrammer
print(f"isAdult: {isAdult}. isProgrammer: {isProgrammer}")
print(f"Is adultProgrammer: {isAdultProgrammer}")


# or
isAdultOrProgrammer = isAdult or isProgrammer
print(f"isAdult: {isAdult}. isProgrammer: {isProgrammer}")
print(f"Is adultProgrammer: {isAdultOrProgrammer}")


print(f"10 == 10 {10 == 10}") #True
val_1 = 10
val_2 = "10"
result = val_1 != val_2
print(f"\"10\" != 10 {result}")

# not - reverses a conditional statement
val_1 = 100
val_2 = "100"
result = not (val_1 == val_2) # same as val_1 != val_2
print(f"not (val_1 == val_2) {result}")

# Conditional Statement using If Statement

# If someone is an adult give person adult access

hasAdultAccess = False
if isAdult:
    hasAdultAccess = True
    print("This line executes")




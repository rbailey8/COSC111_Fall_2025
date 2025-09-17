# Cast Type built-in functions
result = list("Hello")
print(result)

# What is you age
user_age = input("What is your age? ")

# What is your interest
interest = input("What is your top interest? ")

# Are you 18 or older
# True or False
user_age = int(user_age)
print(f"Is user 18 or older {user_age >= 18}")
isAdultAge = user_age >= 18

# Are you younger than 10
# True or False
isKid = user_age <= 10
print(f"Is user underage kid: {isKid}")

checkConditional = isAdultAge and interest == "football"
print(f"Is adult and interested in football {checkConditional}")

# Types of Conditional Operators

val_1 = 100
val_2 = "100.0"
print(val_1 == val_2)

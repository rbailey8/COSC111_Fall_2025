
age = int(input("What is your age: "))
birth_month = input("Birth month: ")
hasAdultAccess = False
hasLimitedAccess = False
above21 = False


# If Statement - below is a if statement conditional block that executes when age is 18+
if age >= 18:
    hasAdultAccess = True
    print("The user access has been update for adult account.")

if age < 21:
    above21 = True
    print("The user is older than 21.")

# If someone has a birth month that is the same as current month then update
isBirthMonth = False
isNotBirthMonth = False
current_month = "September"
if birth_month == current_month:
    isBirthMonth = True
    print("It is currently the user's birth month")

if birth_month != current_month:
    isNotBirthMonth = True
    print("It is not currently the user's birth month")

# Is student between age of 18 and 21 (inclusive)
if age <= 21 and age >= 18:
    print("Student is between 18 and 21")
#  True and True


# If - Else Statement
if age >= 18:
    hasAdultAccess = True
    print("User has adult access")
else: 
    hasLimitedAccess = True
    print("User has limited access only")

# If - Elif - Else Statement
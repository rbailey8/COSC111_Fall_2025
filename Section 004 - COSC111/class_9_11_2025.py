count = 100
count += 20 * 3  # count = count + 20 * 3
count -= 5 # count = count - 5
print(count)

# Uhm Platform

# full_name = input("Enter your full name: ")
# email = input("Email: ")
# age = input("Age: ")
# birth_year = input("Birth year: ")
# phone_number = input("Phone number: ")
# birthday = input("Birthday: ")
# city = input("City: ")
# country
# region
# interests

# print(f"Hi {full_name}, we recieved your info. Your email is {email}, age: {age},  birthday: {birthday}, phone number {phone_number}, city {city}.")

# Let's convert the age to a number
# print(f"birth_year: {birth_year}")
# print(type(birth_year))

# calculated_age = 2025 - int(birth_year)
# print(f"Calculated age: {calculated_age}")
# print(type(calculated_age))

# Convert the data type of a value using special function
result = 10
print(type(result))

result = float(result)
print(type(result))
print(result)
# Convert to string
result = str(result)
print(type(result))
print(result)

result = "52"
# print(type(result))

# result = float(result)
# print(type(result))
# print(result)

# result = "114424353524232342.067676"
# result = float(result)
# print(result)

# interest_1 = input("Interest 1: ")
# interest_2 = input("Interest 2: ")
# interest_3 = input("Interest 3: ")
# interest_4 = input("")
# interest_4 = int(interest_4)
# interests = [interest_1, interest_2, interest_3, interest_4]
# print(interests)




var1 = True # Boolean
print(type(var1))
var2 = "False" # String
print(type(var2))
var3 = input("Enter True or False: ")
print(type(var3)) # Input always returns String
var4 = False # Boolean
print(type(var4))
var5 = "True" # String
print(type(var5))

s = '''
    Helloo
    There
    Family
'''
str = '\n    Helloo\n    There\n    Family'
print(str)
print(s)

# Data types: boolean, interger, float, stringprint()

s = '''baade6
moajo1
brben19
saboa3
yabra4
jobro96
codav18
jafre20
ongat1
ebhen1
tahil25
iamas2
mamat30
mamat29
japhi31
dwric1
emwal3
amwoo8
geand6
jadav147
arhuf3
cajac29
kakys1
demcc41
mamcd14
chmus6
menea2
jarob141
tosob1
kywil51
olyem1
'''
s = s.split()

for name in s:
    print(name + "@morgan.edu")

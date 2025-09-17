
# Augmented Operator form for subtraction
# variable = variable - value
a = 15
a -= 5 * 2 # Same as a = a - 5 * 2

print(a)

# Augmented Operator form for subtraction
# variable = variable + value
b = 28
b += 4 # Same as b = b + 4
print(b)

# Augmented Operator form for subtraction
# variable = variable * value
# S
c = 3
c *= 3 # Same as c = c * 3
print(c)

# PEMDAS
# Parentheis, Exponents, Multuplication, Division, Addition,Subtraction

result = 12/3 + 4 * (8-6)
#        12/3 + 4 *   2
#        12/3 + 8
#          4  + 8 = 12
print(result)

# Power Operation
# 2^2 = 2 * 2 = 4
# 2^3 = 2 * 2 * 2 = 8
result = 2 ** 3  # 2 ** 3 == 2^3
print(result)

x = 2
y = 3
z = (x ** 2) + y * 5
#.     4     + 3 * 5
#       4    + 15
print(z)

a = 25
a //= 3
# a = a // 3 
# a = 25 // 3 = 8
a %= 2
# a = a % 2
# a = 8 % 2 = 0
print(a)

# Creating a new social media 

# Uhm Platform

name = input("Name: ")
dob = input("Date of birth: ")
username = input("Username: ")
password = input("Password: ")

print(f"Hi {name}. We are creating your account with the username: {username} and password: {password}. We also stored you birthday as {dob}")
# location
# email
# phone_number
# is_verified 
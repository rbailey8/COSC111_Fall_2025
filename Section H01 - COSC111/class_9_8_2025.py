# Displays original itinerary

# Alex
alex_password = 'Alex was here'

print(alex_password)
print(f"What password did we use for Alex: {alex_password}")

# Instagram
instagram_password = 'safestPassword'

# CodePath
codepath_password = 'coding'

# Apple Music
apple_music_password = 'Spotify\'s little bro'


# Snake Case
snake_case = "This is snake case format"
new_snake_case_variable = "This is another snake case variable"

# Camel Case
camelCase = "This is how we reference camel case"

str = '''
biaka1
rahmel.bailey
jebar23
robla6
rishi.chopra
dedae1
ledav17
meday1
tadic9
jofle13
jahar224
kihen13
shlee18
tomay3
monko1
chnwa46
akodi1
alsim20
besim4
jaste82
phwar1
'''
people = []
for username in str.split():
    email = username + "@morgan.edu"
    people.append(email)
    print(email)
print(people)
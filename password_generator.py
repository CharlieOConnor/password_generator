# Password generator that includes letters, punctuations and digits as well as
# an error handler for invalid input

import string, random

characters = string.ascii_letters + string.punctuation + string.digits
password = ''

while True:
    try:
        number_of_characters = int(input("How many characters would you like your password to be?: "))
        for i in range(1, number_of_characters):
            password += random.choice(characters)
        print(password)
        break
    except ValueError:
        print("Please only use integers.\n")
        continue

import random
import string


# function to loop through a tuple and convert it to string
def tuple_to_string(tuple):
    variable = ''
    for _ in tuple:
        variable += _
        return variable


def generate_password(min_length, numeric=True, special_char=True):
    # get the required characters in tuple type
    strings = string.ascii_letters,
    digits = string.digits,
    special = string.punctuation
    # change the required characters from tuple type to string type
    letters = tuple_to_string(strings)
    numbers = tuple_to_string(digits)
    # check wether to include numbers or special characters in the generated passwprd
    if numbers:
        letters = letters + numbers
    if special_char:
        letters = letters + special

    has_digits = False
    has_special_char = False
    valid_password = False
    password = ''
    while valid_password != True and len(password) < min_length:
        password = ''
        for _ in range(min_length):
            # generate a random letter from all the alpabet
            new_char = random.choice(letters)
            password += new_char
            # check if the random letter contains numbers or special characters
            if new_char in special:
                has_special_char = True
            if new_char in numbers:
                has_digits = True
            valid_password = True
            if numeric:
                valid_password = has_digits
            if special_char:
                valid_password = valid_password and has_special_char
    return password


user_input = int(input('enter the minimum length: '))
has_number = input('do yo want to include a number (y,n): ').lower() == 'y'
has_special_char = input(
    'do yo want to include a special character (y,n): ').lower() == 'y'
password = generate_password(user_input, has_number, has_special_char)
print(f' the generated password is {password}')

# result = generate_password(5)
# print(result)

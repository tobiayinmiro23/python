import random
trial = 5

print('welcome to this guessing game, guess the random number to win')
start_guess = input('do you want to proceed? y/n: ')
if start_guess.lower() != 'y':
    print('guessing game terminated')
    quit()
invalid_input = True
while invalid_input:
    range = input('selct the top most range for the random number: ')
    if range.isdigit() and int(range) > 0:
        invalid_input = False
        random_number = random.randint(0, int(range))
        print(random_number)
        while trial != 0:
            guess = input('guess the random number: ')
            if int(guess) == random_number:
                print('you\'re correct')
                break
            elif trial == 1:
                print(
                    'user have exceeded the number of trials ')
            elif int(guess) > random_number:
                trial -= 1
                print(
                    f'incorrect guess, you\'re guess is greater than the random number, you have {trial} trials left')
            else:
                trial -= 1
                print(
                    f'incorrect guess, you\'re guess is less than the random number, you have {trial} trials left')
    else:
        print('select a valid number, number must be greater than 0')

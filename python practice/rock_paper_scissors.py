import random
user_score = 0
computer_score = 0
no_of_rounds = 5
options = ['rock', 'paper', 'scissors']

user_input = input(
    'welcome to this rock paper scissors game type \"q\" to quit or any other character to continue: ')
if user_input.lower().strip() == 'q':
    print('rock paper scissors game terminated')
    quit()
while no_of_rounds != 0:
    computer_pick = random.choice(options)
    print(f'no of rounds= {no_of_rounds}')
    print(f'computer option= {computer_pick}')
    print('computer selected an option')
    print(' ')
    invalid_input = True
    while invalid_input:
        user_pick = input('select an option: ')
        print(' ')
        if user_pick not in options:
            print(
                'invalid input, select a valid input, input can only be  rock, paper or scissors ')
            continue
        else:
            break
    if user_pick == computer_pick:
        print('its a tie')
        continue
    elif user_pick == 'rock' and computer_pick == 'scissors':
        user_score += 1
        no_of_rounds -= 1
        print(
            f'you won, computer selected scissors you have {no_of_rounds} rounds left')
    elif user_pick == 'paper' and computer_pick == 'rock':
        user_score += 1
        no_of_rounds -= 1
        print(f'you won, computer selected rock')
    elif user_pick == 'scissors' and computer_pick == 'paper':
        user_score += 1
        no_of_rounds -= 1
        print(f'you won, computer selected paper')
    else:
        computer_score += 1
        no_of_rounds -= 1
        print(f"you lost, you have {no_of_rounds} rounds left")

message = f'Congratulations you won, your score is {user_score}, computer scored {computer_score}' if user_score > computer_score else f'Sorry you lost, your score is {user_score}, computer scored {computer_score}'
print('game terminated')
print(message)

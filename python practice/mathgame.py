import random
import time
min_operand = 2
max_operand = 12
operators = ['+', '-', '*']
problem_count = 5


def generate_problem():
    left_hand = random.randint(min_operand, max_operand)
    right_hand = random.randint(min_operand, max_operand)
    operator = random.choice(operators)
    question = f'{left_hand} {operator} {right_hand} '
    answer = eval(question)
    return question, answer


print('welcome to this maths quiz, answer the following questions')
begin_game = input(
    'press any key to start of press q to cancel: ').strip().lower()
if begin_game == 'q':
    quit()
start_time = time.time()
for i in range(problem_count):
    question, answer = generate_problem()
    while True:
        users_answer = input(f'Question {i + 1}    {question} : ')
        if users_answer == str(answer):
            break
        else:
            print('wrong answer try again')
end_time = time.time()
total_time = round(end_time-start_time, 2)
print(
    f'congratulations you have successfully completed the quiz, you finished in {total_time}s')

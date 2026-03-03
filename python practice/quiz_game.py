score = 0
trial = 0
print('welcome to this quiz game answer correctly to increase your score')
while trial != 5:
    start_quiz = input('do you want to proceed? y/n: ')
    if start_quiz.lower() != 'y':
        print('quiz terminated')
        break
    question4 = input('what is the capital of Nigeria: ')
    if question4.lower().strip() in ['fct abuja', 'abuja', 'fct']:
        # if question4.lower().strip() == 'fct abuja' or question4.lower().strip() == 'abuja':
        print('you\'re correct')
        score += 1
    else:
        print('incorrect answer')
    trial += 1
    question1 = input('what is 2 + 2 ? : ')
    if int(question1) == 4:
        print('you\'re correct')
        score += 1
    else:
        print('incorrect answer')
    trial += 1

    question2 = input('what does URL stand for: ')
    if question2.lower().strip() == 'uniform resource locator':
        print('you\'re correct')
        score += 1
    else:
        print('incorrect answer')
    trial += 1
    question3 = input('what is the largest country in africa: ')
    if question3.lower().strip() == 'nigeria':
        print('you\'re correct')
        score += 1
    else:
        print('incorrect answer')
    trial += 1
    question5 = input('what year did nigeria gain independence ? : ')
    if int(question5) == 1960:
        print('you\'re correct')
        score += 1
    else:
        print('incorrect answer')
    trial += 1
    print(
        f'congratulations you have successfully completed you got {(score/5) * 100}%')

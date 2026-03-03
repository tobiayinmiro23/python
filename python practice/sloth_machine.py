MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input('enter a amount $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('amount must be greater than 0')
        else:
            print('amount must be a number')
    return amount


def get_number_of_lines():
    while True:
        lines = input(
            f'enter the number of lines, line must be between 1 - {MAX_LINES} : ')
        if lines.isdigit():
            lines = int(lines)
            if lines in (1, 2, 3):
                break
            else:
                print(
                    f'enter a valid line number, line must be between 1 - {MAX_LINES}')
        else:
            print('lines must be a number')
    return lines


def get_bet():
    while True:
        amount = input('how much would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if amount in range(1, 101):
                break
            else:
                print(
                    f'amount must be between {MIN_BET} - {MAX_BET}')
        else:
            print('amount must be a number')
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    print(balance, lines)


main()

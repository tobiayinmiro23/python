import turtle
WIDTH, HEIGHT = 500, 500
screen = turtle.Screen()
screen.title('turtle racing game')
screen.setup(WIDTH, HEIGHT)


def get_number_of_racers():
    racers = 0
    while True:
        racers = input('enter number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
            if racers in range(2, 11):
                return racers
            else:
                print('racers must be greater between 2 - 10')
        else:
            print('racers must be a number')


racers = get_number_of_racers()
print(racers)

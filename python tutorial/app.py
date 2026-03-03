import random
from ecommerce.shipping import calculateShipping
import converter
import math
from pathlib import Path
import openpyxl
name = 'tobi'
age = 23
# print(name[1:3])
# if age > 42:
#     print('age is greater')
# else:
#     print('age is not greater')


def name(last, first='tobi',):
    return ('my name is ' + first + ' ' + last)


usersName = name('collins')


# print(usersName)


namesL = ['ade', 'tope', 'basil', 'amina', 'wale', 'tope']
namesS = {'wale', 'timi', 'sam', 'wale', 'tobi', 'sam'}
namesT = ('don', 'rizzo', 'rally', 'smith')
namesD = {
    'name': 'ade',
    'age': 23,
    'sex': 'male',
    'level': 14
}


map_list = map(lambda x: x+'!', namesL)
# print(map_list)
# print(list(map_list))


def greater_than_4(str):
    return len(str) > 4


filter_list = filter(greater_than_4, namesL)
# print(list(filter_list))

# for index, item in enumerate(namesL):
# print(f'index is {index} item is {item}')


def starts_with(list):
    if list.startswith('a'):
        return list


# a = filter(lambda x: x.startswith('a'), namesL)


# a = filter(starts_with, namesL)
# print(list(a))

# print('ade' in namesL)

# print(f"the list of names are {namesL}")

# for x in range(12):
#     print(x)


# i = 5
# while i > 1:
#     print(i)
#     i -= 1


strTest = 'i am a string'

# print(abs(-3.5))
# print(math.cos(4))
# user_name = input('Enter your name:')
# print(f'users name is {user_name}')

score = 21
message = 'you are eligble' if score > 30 else 'you are not eligble'
# print(message)

# if 20 < score < 60:
# if (score > 70 and score < 60) or score == 50:
# print('score within range')
# else:
# print('score not within range')


# for no in range(1, 11):
#     if no % 2 != 0:
#         print(no)
# else:
#     print('we have four even numbers')


# users_command = ''
# while users_command != 'quit':
#     users_command = input('enter command: ').lower()
#     print(users_command)

file = open('test.py', 'w')
file.write('writing with python')
file.close()


def get_total(*numbers):
    total = 0
    for i in numbers:
        total += i
    print(total)


# get_total(2, 4, 4, 5, 1)

# allowed = True
# while allowed:
#     user_input = input('>').lower()
#     if user_input == 'help':
#         print('start - to start the car\nstop - to stop the car\nquit - to quit ')
#     elif user_input == 'quit':
#         allowed = False
#     else:
#         print('invalid command')


# numbers = [2, 4, 5, 2, 1, 8, 2, 3]
# new_number = []
# for x in numbers:
#     if x not in new_number:
#         new_number.append(x)
# print(new_number)

# largest = numbers[0]
# for x in numbers:
#     if x > largest:
#         largest = x
# print(largest)
let = [1, 2, 3]
a, b, c = let
# print(a, b)

numbers = {
    "1": 'one',
    '2': 'two',
    '3': 'three'
}
exists = numbers.get('19', 'ninteen')
# print(exists)

# new_number = ''
# users_input = input('enter number:')
# for x in users_input:
#     new_number += numbers.get(x) + ''
# print(new_number)


# try:
#     print(mm)
# except NameError:
#     print('an error occured')

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def getCourse(self):
        print(f'im studying {self.course}')

    def getStudentName(self):
        print('hi my name is', self.name)


stud = Student('ayinmiro tobi collins', 'Computer Science')
# print(stud.course)


class Person(Student):
    # def __init__(self, name):
    #     self.name = name

    def talk(self):
        print(f'hi there how do you do, nice to meet you')


person1 = Person('john', 'engineering')
# print(person1.course)

# person1.getStudentName()
# person2 = Person('john CW')
# person2.talk()

# converter.kg_to_pb(80)

# list = [2, 4, 4, 5, 1]
# print(max(list))
# calculateShipping()
# print(random.choice(namesL))


class Dice:

    def roll(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1}, {dice2})',)

# player = Dice()
# player.roll()


# path = Path('ecommerce')
# print(path.exists())
# for i in path.glob('*'):
#     print(i)

str = 'oop means object oriented programming'
# print('11'.join(str))

arr = [12, 0.2, 7, 3, 5, 6]
# arr[2:4] = ['test1', 'test2']
# arr.pop(5)
print(sorted(arr, reverse=True))
# a, b, *c = arr
# print(arr)
# [print(x) for x in arr if x > 3]

# (lambda x: print(x ** 3))(3)

# print('hehy', 'hi', 'ho', sep='|')

item = ['A', 'B', 'C', 'D', 'E']
b = [i for i in item if i != 'B']
print(b)

# item2 = []
# for i in item:
#     if i == 'B':
#         continue
#     else:
#         item2.append(i)

# print(item2)

result = filter(lambda x: x != 'B', item)
print(list(result))

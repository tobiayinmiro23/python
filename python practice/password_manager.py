from pathlib import Path
from cryptography.fernet import Fernet
p = Path()
print(p.exists())
all_files = p.glob('*')
print(list(all_files))


master_password = input('welcome user, what is the master password?: ')


def write_key():
    key = Fernet.generate_key()
    with open('admin.key', 'wb') as key_file:
        key_file.write(key)


def read_key():
    with open('admin.key', 'rb') as key:
        key = key.read()
        return key


key = read_key()
fer = Fernet(key)


def add():
    user_name = input('add user name:  ').lower().strip()
    password = input('add password:  ').lower().strip()
    with open('passwords.txt', 'a') as file:
        file.write(
            f'{user_name} | {fer.encrypt(password.encode()).decode()} \n')
    print('account successfully created')


def view():
    with open('passwords.txt', 'r') as files:
        for lines in files.readlines():
            result = lines.rstrip().split('|')
            username, password = result
            print(username, fer.decrypt(password).decode())


while True:
    mode = input('would you like to add a new password or view am existing password, type "view" to view password, "add" it add password and "q" to quit:  ').lower().strip()
    if mode == 'q':
        break
    if mode == 'view':
        view()
        break
    elif mode == 'add':
        add()
        break
    else:
        print('invalid input')
        continue

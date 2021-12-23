from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key


pwd = input("What is the password: ")

key = load_key() + pwd.encode()

fer = Fernet(key)


def view():
    with open('password.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print("User: ", user, " | Password: ",
                  str(fer.decrypt(passw.encode())))


def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open('password.txt', 'a') as file:
        file.write(f"{name} | {str(fer.encrypt(password.encode()))}\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing password (view, add) press q to quit: ").lower()

    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode.")
        continue

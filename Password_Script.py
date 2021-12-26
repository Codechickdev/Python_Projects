import random
import pyautogui

choice = int(input("Enter 1 to crack the password. 2 to Generate password. 3 to exit: "))

while True:
    if choice == 1:
        chars = ' a b c d e f g h i j k l m n o p q r s t u v w x y z '
        chars_list = list(chars)

        password = pyautogui.password("Enter your password: ")
        guess_pw = ''
        count = 1

        while(guess_pw != password):
            guess_pw = random.choices(chars_list, k=len(password))
            print(f"=== {str(guess_pw)} ===")
            count +=1
            if guess_pw == password:
                print(f"Your password is {guess_pw}")
                print(f"It took {count} seconds to crack your password")
                break

    elif choice == 2:
        len_input = int(input("Enter the length of the password: "))
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        p = "".join(random.sample(s, len_input))
        print(f"Your password is generated -- {p}")

    elif choice == 3:
        break

    else:
        print("Invalid Input")

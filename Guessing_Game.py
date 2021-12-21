import random

while True:
    random_guess = random.randint(1, 10)
    player = int(input("Enter a number between 1 to 10: "))

    if player == random_guess:
        print("You won!")
    else:
        print("You lose")

    res = input("Do you want to play again? (yes or no): ")
    if res != 'yes' or res == 'y':
        break

print("Thanks for playing")

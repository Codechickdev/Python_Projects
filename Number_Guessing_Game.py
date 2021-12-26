import random

count = 0

while True:
    guessed_number = random.randint(1, 11)
    player_guess = int(input("Enter a number between 1 to 10: "))
    try:

        if count == 3:
            print("You turned out")
            break

        if player_guess == guessed_number:
            print("You won!")
            break
        
        else:
            print("You guessed it wrong, Try again")
            count += 1

    except ValueError:
        print("You have entered invalid input")
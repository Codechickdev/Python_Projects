def message_encoder(message):
    message_array = []
    for char in message:
        message_array.append(ord(char))
    return message_array

while True:
    print("Enter 1 to Encode or 2 to Exit: ")
    choice = int(input("You input: "))
    if choice == 1:
        message_input = input("Enter the message you need to Encode: ")
        print(message_encoder(message_input))
    elif choice == 2:
        print("Thanks for running this program")
        break
    else:
        print("Invalid Input")
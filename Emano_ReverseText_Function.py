def reverse_text():
    while True:
        user_input = input("Enter a string: ")

        if user_input.isdigit():
            print("Error Reported! Enter text only.")
        else:
            reversed_text = user_input[::-1]
            print("Output:", reversed_text)
            break

reverse_text()

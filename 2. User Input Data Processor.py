
# Task 1: Input Length Validator

def input_lenth_validator():
    first_name = input("Enter your first name: ")
    last_name = input(" Enter your last name :")

    if len(first_name) < 2 :
        print(" Error: At least 2 characters in the First name.")
    elif len(last_name) < 2 :
        print("Error: At least 2 characters in the last name.")
    else:
        print(f" Hello, {first_name} {last_name}!")

input_lenth_validator()
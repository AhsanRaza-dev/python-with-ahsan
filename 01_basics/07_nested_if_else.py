# Nested if else

email = input("Enter your email: ")

# Basic email validation using nested if-else
if '@' in email and email.count('@') == 1 and '.' in email.split('@')[-1]:
    password = input("Enter your password: ")

    if email == "pythonwithahsan@gmail.com" and password == "1234":
        print("Welcome to the Python course!")
    elif email == "pythonwithahsan@gmail.com" and password != "1234":
        print("Invalid Password, Enter the correct password to login")
        password = input("Enter password again: ")
        if password == "1234":
            print("Finally Correct!")
        else:
            print("Still Incorrect Password")
    else:
        print("Incorrect credentials to login")

else:
    print("Enter a valid Email")

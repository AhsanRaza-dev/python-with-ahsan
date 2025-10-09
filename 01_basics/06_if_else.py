# if else conditions 

email = input("Enter your email: ")
password = input("Enter your password: ")

if email == "pythonwithahsan@gmail.com" and password == "1234":
    print("Welcome to the python course")
elif email =="pythonwithahsan@gmail.com" and password != "1234":
    print("Invalid Password, Enter the correct password to login")
else:
    print("Incorect credentials to login")

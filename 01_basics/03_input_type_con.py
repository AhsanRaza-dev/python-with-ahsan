# input fuction always returns string it is used to take input from user
name = input("Enter your name: ")  # input function
age = input("Enter your age: ")    # input function
height = input("Enter your height in cm: ")  # input function

# all these inputs takes the input form the user in string format
print("Your name is: ", name)
print("Your age is: ", age) 
print("Your height is: ", height, "cm")


# type checking
print("Data type of name is: ", type(name))  # string
print("Data type of age is: ", type(age))    # string 

# type conversion
# types
# 1. implicit type conversion (done by python automatically)
# 2. explicit type conversion (done by user manually)

# implicit type conversion
num1 = 10    # integer
num2 = 3.14  # float
result = num1 + num2  # implicit type conversion (integer to float)
print("Result of num1 + num2 is: ", result)  # float
print("Data type of result is: ", type(result))  # float
# the result will be float because in implicit type conversion python converts the integer to float, python is smart enough to do this he gets the data type of both the variables and converts the integer to float because float is more precise than integer

# explicit type conversion
type(age)  # string

age = int(age)  # converting string to integer as we get the age in string format from the user
print(age)

height = float(height)  # converting string to float
print(type(height))
print(height)

print(list("Hello World!, You are learning Python from Ahsan Raza") ) # converting string to list it will contain the blank spaces as well as a character


'''
note:
1. type conversion is not the permanent operation it is temporary
2. It just create the new value but the original value remains the same
3. if you want to make the type conversion permanent then you have to assign the converted value to the original variable
4. if you want to convert the string to int or float then make sure that the string contains only numeric characters    
5. if the string contains non-numeric characters then it will throw an error while converting to int or float
'''
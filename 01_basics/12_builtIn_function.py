# 1. Print Function
print("Hello World, Welcome to the python course")

# 2. Input Function
input("Enter your input: ")

# 3. Type Function
age = 24
print(type(age))

# 4. Int Function
print(int(5.6))  # this will convert these value to the int

# 5. abs Function (absalute function) more likly the modulus function
print(abs(-4))  #it will convert the -4 to 4

# 6. power function
print(pow(2,3)) # it will show the answer 8 like 2*2*2 = 8

# 7. Min/Max Functions

print(min([1,23,432,52,12]))
print(max([1,23,432,52,12]))
min("Lahore") # that will determine the min value based on tha ASCII value
max("Lahore") # that will determine the max value based on tha ASCII value

# 8. Round Function
c = 22/7
print(c)  # that will print the value of c = 3.142857142857143
print(round(c,2))  # it will help as the take round numbers after the decimal in this it will show only two numbers after point

# 9. Divmod Function
print(divmod(5,2))  # Return the tuple (x//y, x%y). Invariant: div*y + mod == x.

# 10. Binary / Octa / Hexa Functions
bin(3) # it will genrate the binary code for the 3
hex(3) # it will genrate the Hexa code for the 3
oct(3) # it will genrate the Octa code for the 3

# 11. Id Function
a = 10 
id(a) # it will give you the memory address of the variable a

# 12. Ord Fucntion
ord(12)  # Return the ordinal value of a character.If the argument is a one-character string, return the Unicode code point of that character. If the argument is a bytes or bytearray object of length 1, return its single byte value.

# 13. Lenth function
a = 'This is the python course'
print(len(a)) # that will print the lenth of the variable 

# 14.  Sum Function 
sum([1,23,42,52,12])  # it will give sum 

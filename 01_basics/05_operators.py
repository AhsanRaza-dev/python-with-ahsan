# Operators in Python
'''
1. Arithmetic Operators
    a. Addition (+)
    b. Subtraction (-)
    c. Multiplication (*)
    d. Division (/)
    e. Modulus (%)
    f. Floor Division (//)
    g. Exponentiation (**)
2. Comparison Operators
    a. Equal to (==)
    b. Not equal to (!=)
    c. Greater than (>)
    d. Less than (<)
    e. Greater than or equal to (>=)
    f. Less than or equal to (<=)
3. Logical Operators
    a. And (and)
    b. Or (or)
    c. Not (not)
4. Bitwise Operators
    a. AND (&)
    b. OR (|)
    c. NOT (~)
    d. XOR (^)
    e. Left Shift (<<)
    f. Right Shift (>>)
5. Assignment Operators
    a. Assign (=)
    b. Add and Assign (+=)
    c. Subtract and Assign (-=)
    d. Multiply and Assign (*=)
    e. Divide and Assign (/=)
    f. Modulus and Assign (%=)
    g. Floor Divide and Assign (//=)
    h. Exponentiate and Assign (**=)

'''
# Arithmetic Operators
x = 10
y = 20

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x//y)
print(x**y)



# Logical operators
x = True
y = False
# or operator
print(x or y)
# AND operator
print(x and y)
# Not operator
print(not y)

# Bitwise operators 
# only works on binary values

x = 2
y = 3

print(x & y)  #here & is bitwise operator. AND is Logical operator
print(x|y)
print(x>>2)
print(x<<3)
print(~x)
 

'''
010 -> 2's binary
110 -> 3's binary
---
010 -> 2's binary 
'''

# Assignment operators 
a = 3
print(a)

a+=3
# a=a+3
print(a)

a-=3
print(a)
a&=4
print(a)
a*=4
print(a)
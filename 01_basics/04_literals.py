# Literals in python 
# Literals are the data that we use in our program
# Literals are the representation of data in a program

'''
1. Numeric Literals
    a. Integer Literals
    b. Float Literals
    c. Complex Literals
2. String Literals
3. Boolean Literals
    a. True
    b. False
4. Special Literals
    a. None
'''

# 1. Numeric Literals
a = 0b1010  # binary literal (base 2)
b = 100     # decimal literal (base 10)
c = 0o310   # octal literal (base 8)
d = 0x12c   # hexadecimal literal (base 16)

# float literals
e = 3.14    # float literal
f = 2.5e2   # float literal (2.5 * 10^2 = 250.0)
g = 2.5e-2  # float literal (2.5 * 10^-2 = 0.025)

# complex literals
h = 3 + 4j  # complex literal (3 is real part and 4j is imaginary part)
i = 5j      # complex literal (0 + 5j)  
j = -2.5j   # complex literal (0 - 2.5j)


print("Numeric Literals:",a,b,c)
print("Float Literals:",e,f,g)
print("Complex Literals:",h,i,j)



# 2. String Literals
str1 = "Hello, World!"          # double quotes
str2 = 'Hello, World!'          # single quotes
str3 = """This is the multi line string with more than one line"""  # triple double quotes (multi-line string) used for docstring 
str4 = '''This is the multi line string with more than one line'''  # triple single quotes (multi-line string)

unicode = u'\U0001f600\U0001f606\U0001F923'  # unicode string
raw_str = r'C:\newfolder\test'  # raw string (ignores escape

print("String Literals:", str1)
print("String Literals:", str2)
print("String Literals:", str3)
print("String Literals:", str4)
print("Unicode String:", unicode)
print("Raw String:", raw_str)  # prints the backslashes as well

# 3. Boolean Literals
bool1 = True
bool2 = False

a = True + 5  # True is treated as 1
b = False + 5 # False is treated as 0
print("Boolean Arithmetic:", a)  # 1 + 5 = 6
print("Boolean Arithmetic:", b)  # 0 + 5 = 5
print("Boolean Literals:", bool1)
print("Boolean Literals:", bool2)

# 4. Special Literals
special = None  # None is used to represent the absence of value
print("Special Literal:", special)
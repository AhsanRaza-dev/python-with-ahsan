a = 'lahore'

# common funtions
print(len(a))
print(max(a))
print(min(a))

print(sorted(a, reverse=True))

# String Specific functions

# 1. Captilization
print(a.capitalize()) # this will captilize the first char

# 2. title
print(a.title()) # this will captilize the entire string

# 3. upper
print(a.upper())  #it will convert the entire string in to capital

# 4. lower
print(a.lower())  #it will convert the entire string in to Lower


# 5. count
b = 'This is the python course which will help you in getting the skills in the field of AI'.count('t')
print(b)

# 6. Find/index
b = 'This is the python course which will help you in getting the skills in the field of AI'.find('t') #it will give you the index of first occurance of the char
print(b) 


# 7. format
# it is used where we don't know which value will come
b = 'This is the {} course which will help you in getting the skills in the field of {}'.format('python','AI')
print(b)


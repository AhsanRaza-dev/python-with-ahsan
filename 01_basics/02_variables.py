# In python their will be the value momory address not variable 
# we have to check the naming convention for each variable i.e. 1ahsan, @ahsan are invalid variable names
# valid variable names are ahsan1, _ahsan, ahsan_1 etc.
# variable names are case sensitive i.e. Ahsan and ahsan are two different variables
# variable names should not be a keyword i.e. if, else, for, while etc are invalid variable names
# valid variable names are my_var, myVar, my-var etc.
 
a = 10
b = 10

print(a + b)
print(id(a))  # id() function is used to get the memory address of a variable
print(id(b))  # both a and b will have the same memory address because they have the same value
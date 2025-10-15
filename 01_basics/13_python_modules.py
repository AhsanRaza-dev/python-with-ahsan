'''
what are the modules?
-> A file contains a set of functions you want to incude in your appications
1. Math
2. Random
3. OS
4. time
'''
import math # this is used to perform mathametical operations in side your program
import random
import time
import os

'''Some Math functions '''
print(math.pi) #this will print the value of pi
print(math.factorial)
print(math.e)
print(math.ceil(0.5))
print(math.floor(0.6))   
print(math.sqrt(100))   

''' Some Random Functions '''
print(random.randint(1,100)) # IT WILL print the random number between the range of 1 to 100 every time this will genrate the new number

a = [1,2,3,4,5]
random.shuffle(a) # this will shuffle the list randomly
print(a)

''' Time functions'''
print(time.time()) # this will gice the time from 1st jan 1970 midnight to today 

print(time.ctime())  # this will tell you the exect time in you regoin 

# sleep function used to add some deleay in any thing, in following code the hello will print and the world will print with the some delay

print("HEllo")
time.sleep(2)
print("World")


'''OS'''
print(os.getcwd())  # will print the current directory

print(os.listdir()) # will print the files inside the dir
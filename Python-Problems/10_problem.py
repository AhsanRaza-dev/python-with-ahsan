import random #this is used for the random number genration

jackot = random.randint(1,100) #it will genrate the number between 1 to 100
guess = int(input('Lets enter to guess the number: '))

while guess !=jackot:
    if guess<jackot:
        print("Guess Higher")
    else:
        print('Guess Lower')
    guess = int(input('Oho wronge number, Guess again: '))

print("Great that's a right guess")
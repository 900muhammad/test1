import random
def askForGuess():
    while True:
        guess = input('>')
        if guess.isdecimal():
            return int(guess)
        print('Please enter a number between 1 and 100')
        print()
secretNumber = random.randint(1,100)
print('i am thinking of a number between 1 and 100')
for x in range(10):
    print('You have {} guesses .Take a guess.'.format(10 - x))
    guess = askForGuess()
    if guess == secretNumber:
        break
    if guess < secretNumber:
        print('GUESS IS TOO LOW')   
    if guess > secretNumber:
        print('GUESS IS TOO HIGH')

if guess == secretNumber:
        print('GOOD:THAT IS CORRECT')  
else:
    print('GAME OVER')
        
    

askForGuess()
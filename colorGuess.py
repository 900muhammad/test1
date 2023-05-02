import random 
colors = 'red orange green blue indigo violet'
def ColorGuess():
    while True:
        guess = input('>>')
        if guess  in colors:
            return str(colors)
        print('I am guessing of a rainbow color')
        print()
rainbowColor = random.choice(colors)
print('I am guessing a color in the rainbow')
for x in range(20):
    print('You have {} guesses left'.format(20 - x))
    guess = ColorGuess()
    if guess == ColorGuess():
        break
    if guess > len(colors):
        print("YOU ARE {} COLORS AHEAD".format(colors - 1))
    if guess  < len(colors):
        print('YOU ARE {} COLORS BEHIND'.format(colors - 1))

if guess == rainbowColor:
    print('you are correct!colorful!')  
else:
    print('OUTTA TIME')


            
        

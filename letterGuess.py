import random
letter = 'A B C D E F G H I G K L M N O P Q R S T U V W X Y Z'
def LetterGuess():
    while True:
        guess = input('>')
        if guess.isalpha():
         return str(guess.isalpha)
        print('Please enter a letter a capital letter between A and Z')
        print()
secretLetter = random.choice(letter)
print('I am thinking of a letter between A and Z')
for x in range(12):
   print('You have {} guesses left.'.format(12 - x))
   guess = LetterGuess()
   if guess == secretLetter:
      break

if guess == secretLetter:
      print('CORRECT!')
elif guess != secretLetter:
      print('GUESSING OVER')
    

LetterGuess()







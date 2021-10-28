import random

lives = 9
words = ['Spain', 'Italy', 'India', 'China', 'Egypt', 'Libya']
secret_word = random.choice(words)
clue = list('?????')
heart_symbol = u'\u2764'
correct = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

while lives > 0:
    print(clue)
    print('Lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the Country: ')

    if guess == secret_word:
        correct = True
        break
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect. You lost a life')
        lives = lives - 1

if correct:
    print('You won! The Country was ' + secret_word)

else:
    print('You lost! The Country was ' + secret_word)

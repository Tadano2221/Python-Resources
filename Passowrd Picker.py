import random
import string

words = ['eftfdkjxx', 'ffdrgergerg', 'fewegf', 'wfwegwefeg', 'rgegrgerg', 'ergerge', 'regergerg', 'elwkhyr']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(' ')', '-', '_', '+', '=', '<', '>', '?', '~']

print('Welcome topassword picker')

while True:
    word = random.choice(words)
    symbol = random.choice(symbols)
    number = random.randrange(0, 100000)
    special_char = random.choice(string.punctuation)

    password = word + symbol + str(number) + special_char
    print('Your New Password is %s' % password)

    response = input('Whould you like another password? Type yes or no')
    if response == 'n':
        break

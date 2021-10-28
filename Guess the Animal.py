def check_guess (guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower () == answer.lower ():
            print('Correct Answer')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                  guess = input('Sorry wrong answer. Try again')
            attempt = attempt + 1
                

    if attempt == 3:
        print ('The correct answer is' + answer)

score = 0
print('Guess the Animal')
guess1 = input('Which animal never dies ')
check_guess (guess1, 'Jellyfish')
guess2=input('Which Rhino is the most endangered?')
check_guess (guess2, 'Javan Rhino')
guess3=input('Which animal melts at 5°C?')
check_guess (guess3, 'Ice Worm')
             
print('Your score is' + str(score))


def Multiplication_Game():
    x = input('value?')
    table = x
    for i in range(1, 13):
        print('What\'s', i, 'x', table, '?')
        guess = input()
        if guess == 'stop':
            break
        if guess == 'skip':
            print('Skipping')
            continue
        ans = i * table
        if int(guess) == ans:
            print('Correct!')
        else:
            print('No, it\'s', ans)
    print('Finished')
Multiplication_Game()


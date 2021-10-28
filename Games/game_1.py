def ghost_game():
    #Ghost Game
    from random import randint
    print('Ghost game')
    feeling_brave = True
    score = 0
    while feeling_brave:
        ghost_door = randint(1, 5)
        print('Three doors ahead')
        print('A ghost behind one')
        print('Which door do you open')
        door = input('1, 2 , 3, 4, 5?')
        door_num = int(door)
        if door_num == ghost_door:
            print('GHOST!')
            feeling_brave = False
        else:
            print('No Ghost!')
            print('You enter the next room')
            score = score + 1
def identity_game():
    age = input('age?')
    print('I am' + age)
    Name = input('name')
    print('I am' + Name)
    print('Hello,' + age + 'year old' + Name)
def monster_game():
    answer = 'y'
    while answer == 'y':
        print('Stay very still')
        answer = input('Is the monster friendly? (y/n)')
    print('Run away!')
def Forever_typing():
    while True:
        answer = input('Type a word and press enter: ')
        print('Please do not type \'' + answer + 'again')






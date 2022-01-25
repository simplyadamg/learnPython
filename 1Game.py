import random
yn = 'Y'
print ('Hello what is your name?')
name = input()
def game():
    print ('What would you like the range of your numbers to be?')
    print ('High Number')
    highNum = input()
    print ('Low Number')
    lowNum = input()
    secretNum = random.randint(int(lowNum), int(highNum))
    print ('The number I\'m thinking of is between ' + str(lowNum) + ' and ' + str(highNum))
    guess = secretNum+1
    i = 0
    while int(guess) != secretNum:
        print ('What is your guess?')
        guess = input()
        i = i + 1
        if int(guess) > secretNum:
            print ('Too High')
        elif int(guess) < secretNum:
            print ('Too low')
        elif int(guess) == secretNum:
            print ('You Win!')


    print ('Great Job ' + name + ' the secret number is ' + str(secretNum) + ' It took you ' + str(i) + ' tries to guess the number')
    print('Would you like to play again?')
    yn = input()
    if yn == 'Y':
        game()
    elif yn != 'Y':
        print ('Thanks for playing!')
        exit()


def toPlay():
    yn = 'Y'
    while yn != 'N':
        print ('Hello ' + name + ' I\'m computer would you like to play a fun game? Y/N')
        yn=input()
        if yn == 'Y':
            game()
        else:
            yn = 'N'
toPlay()


import pyperclip
# from the random linbrary import all things
# and make them usable without calling the function
# ie. random.randint(x)
# from random import *
print('Remember unless I fucked up')
print('you should be able to type Exit in any of these prorams to quit')


def lessons():
    i = 1
    while i == 1:
        print('Which lesson would you like to access?')
        print('6 - while, break, continue')
        print('7b - for, in, range ')
        print('8 - ')
        print('8b - ')
        # print ('7 - ')
        # print ('7 - ')
        # print ('7 - ')
        # print ('7 - ')
        # print ('7 - ')

        i = input()
        if i == 'Exit':
            return
        if i == str(6):
            lesson6()
        if i == str(7):
            lesson7()
        if i == '7b':
            lesson7b()
        if i == str(8):
            lesson8()
        if i == '8b':
            lesson8b()
        if i == str(9):
            lesson9()
        if i == str(10):
            lesson10()
        if i == str(11):
            lesson11()
        if i == str(12):
            lesson12()
        if i == str(13):
            lesson13()
        if i == str(14):
            lesson14()


def lesson6():
    # vocab: while
    # vocab: break
    # vocab: continue
    print('This is lesson 6')
    x = 0
    while x != 'x':
        print('What value would you like to make X?')
        x = input()
        if x == 'Exit':
            break
        elif x == 'Skip':
            continue
        elif x != 'Exit':
            print('X is currently equal to ' + str(x))
            print('Type Exit for the program to break.', end='')
            print(' Or you can type \'x\' for the loop to be satisfied')


def lesson7():
    # vocab: for
    # vocab: in
    # vocab: range
    x = 0
    i = 1
    word = ''
    print('This is lesson 7')
    print('Pick a word')
    word = input()
    print('How many times would you like to see that word on the screen?')
    x = input()
    for i in range(int(x)):
        print(str(i+1) + ' Your word is ' + word)
    if x == 'Exit':
        print('Retun?')
        return

    total = 0
    for num in range(101):
        print(str(num) + ' plus ' + str(total) + ' equals ')
        total = num+total
        print(total)
    print(total)
    # Range is of the range data type and it can include multiple inputs
    # Range (0,10) starts at 0 and goes to 10
    # Range (0,10,2) Starts at 0 goes to 10 and increases by 2
    # (the step value) for each itteration
    lesson7()


def lesson7b():
    print('What number would you like your loop to start at?')
    a = input()
    print('What number would you like your loop to end at?')
    b = input()
    print('What number would you like to count by (the step value)?')
    c = input()
    print('How many times would you like this loop to loop?')
    for i in range(int(a), int(b), int(c)):
        print('We are on step number ' + str(i))
        print(' the next number will be our current step plus ' + str(c))


def lesson8():
    # vocab: import
    # vocab: from
    # vocab: random
    # vocab: exit (sys.exit)
    import random
    print('How many random numbers would you like to see?')
    j = input()
    print('Here are your ' + str(j) + ' random numbers.')
    for i in range(1, int(j)+1):
        print('Here\'s your random numbe #'+str(i))
        x = random.randint(1, 10)
        print(x)
        # You can also import multiple modlues
        # by seperating them with commas after improt
    import sys
    import os
    import math
    # You can also use the from statement here:
    # from random import *
    # This imports the random function (or any function you want to import)
    # but makes it so you don't have to type the
    # name of the library at the beginning of the statement.
    # See the statement before the function
    print('Input a word you want to see')
    print('This number will appear a random number of times')
    print('Up to five times')
    word = input()
    for i in range(random.randint(1, 5)):
        print(i)
        print(word)
    print('do you want to exit the program?')
    leave = input()
    if leave == 'Y':
        sys.exit()
        # sys call... by imnporting sys and then using exit to end a program.
    elif leave == 'N':
        lessons()
    else:
        lesson8()


# Let's you copy stuff to the clipbaord.
def lesson8b():
    print('lesson 8b')
    pyperclip.paste()


def lesson9():
    print('lesson 9')


def lesson10():
    print('lesson 10')


def lesson11():
    print('lesson 11')


def lesson12():
    print('lesson 12')


def lesson13():
    print('lesson 13')


def lesson14():
    print('lesson 14')


lessons()

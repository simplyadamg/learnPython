# This program says hello and ask for my name
#
# operators
# == Equal to
# != not equal to
# <
# >
# <=
# >=
# Booleans: And, or, not

# hatesJobYN = ''
# while hatesJobYN != 'Y' and hatesJobYN != 'N':
#     print ('Do you hate your job? Y/N')
#     hatesJobYN  = input()
#     if hatesJobYN != 'Y' or 'N':
#         print('You must enter Y or N')
# if hatesJobYN == 'Y':
#     print ('On a sacle from 1 - 10 how much do you hate your job? ')
#     hatesJobAmt = input()
#     print ('lets see if we can cut that in half down to: ' + str(int(hatesJobAmt)/2))
#
#
#     print ('How many hours have you been studying this?')
#     beenHere = input() #input always creates a string
#     print ('Damn dude ' + beenHere + ' hours is a long time')
#     print ('I have been working on this for ' + str(int(beenHere) + 2) + ' hours')
#     print ('Well someone has been doing the exact same thing for at least ' + str(int(beenHere)+12) + ' months')
#
#     print ('How many hours do you work per week?')
#     hoursWeekly = input()
#     print ('Thats too many hours dude, you should be working less than ' + str(int(hoursWeekly)/2) + ' hours per week.')
# else:
#     print ('Well at least you enjoy your work.')
# delServ = ''
# print ('Do you want to delete the server? Yes or YES!')
# delServ = input()
# if delServ != 'YES!':
#     while delServ != 'YES!':
#         print ('You\'re not excited about deleting the server, i\'ve got aaaall night')
#         print ('Do you want to delete the server? Yes or YES!')
#         delServ = input()
# print ('I went and got a strong electromagnet what should I do with it?')
# print ('1. Chicken out')
# print ('2. Plug that fucker in and let er rip')
# useMag = input()
# while useMag != int('1'):
#     print ('You\'re not excited about deleting the server, i\'ve got aaaall night')
#     print ('Should I use the magnet? 1 or 2')
#     useMag = input()
# if useMag == '1':
#     print ('You go home like a bitch and jerk off again')
# if useMag == '2':
#     print ('You bring the whole company down and everyone celebrates')

# days=0
# while days<8:
#     print ('How many days per week would you be working out ideally?')
#     days = input()
#     if int(days) > 7:
#         print ('There arent more than 7 days in a week.')
#     elif int(days) > 6:
#         print ('you will get burned out fast')
#     elif int(days) > 5:
#         print ('you are on fire')
#     elif int(days) > 3:
#         print ('At least you are trying')
#         print ('you have a great work eithic')
#     elif int(days) > 0:
#         print ('Couch potato')
#
# spam = 0
# while spam < 5:
#     print ('hi' + str(spam))
#     spam = spam +1
#

# def fuckIt():
#     i = 0
#     while i < 10:
#         if i == 1:
#             print ('fuck it ' + str(i) + ' time')
#         if i > 1:
#             print ('fuck it ' + str(i) + ' times')
#         i = i+1
# fuckIt()
# fuckIt()
# fuckIt()

#crashes when I enter a string for input
days = 0
while int(days) < 100:
    print ('How many days per week would you work out ideally?')
    days = input()
    if int(days)>100:
        print('Exit')
    elif int(days) > 7:
        print ('There arent more than 7 days in a week.')
    elif int(days) > 5:
        print ('you will get burned out fast')
    elif int(days) > 3:
        print ('you are on fire')
    elif int(days) > 1:
        print ('Solid work eithic')
    elif int(days) > 0:
        print ('At least you\'re trying')
    elif int(days) == 0:
        print ('Couch potato')

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

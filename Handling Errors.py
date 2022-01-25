# def div42by(divideBy):
#     try:
#         return 42/divideBy
#     except ZeroDivisionError:
#         print ('Div zero error')
# for i in range(3,-3,-1):
#         print(div42by(i))
i=1
while i == True:
    i=1
    print ('How many hours will you work this week?')
    yourN = input()
    try:
        if int(yourN) > 30:
            print ('That\'s too many hours dude you\'re going to have a heart attack')
            i=0
        elif int(yourN) <= 30:
            print('That is a much more reasonable amt of time')
            i=0
        elif int(yourN) == 0:
            print ('You could proabbly work a bit more')
            i=0
        elif int(yourN) < 0:
            print ('You have gone back in time')
            i=0
    except ValueError:
        print ('You must enter a whole number, no letters')

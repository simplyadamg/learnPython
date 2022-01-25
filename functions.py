def fuckIt(name):
    i = 0
    while i <= 3:
        if i == 1:
            print ('fuck it ' + str(i) + ' time ' + name)
        if i > 1:
            print ('fuck it ' + str(i) + ' times ' + name)
        i = i+1
fuckIt('Jack')
fuckIt('Jane')
fuckIt('Dick')

def plusONe(number):
    return number +1
newNumnber = plusONe(6)
print (newNumnber)
print ('chemicals','rust','grease', end='. ', sep='; ')
print ('These are the things that sanchem deals in')

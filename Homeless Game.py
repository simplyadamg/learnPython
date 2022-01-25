#systems type stuff goes up here


import os
import random

def clear():
    os.system('clear')
clear()

# Global things that change over time stats inventory maybe healing, maybe getting a job or an aparmtnet


timeOfDay=['early morning','mid morning','late morning','mid day','late afternoon','early evening','late evening','mid night']
currentTimeOfDay=timeOfDay[1]
ineventory = [['snickers bar','half chipotle burrito'],[1,2]]
stats = [['Energy','Food','Shelter','Money','Sleep'],[10,10,10,10,10]]
places=['park','highway','tent','panera','lake','uptown']
currentLocation=places[2]
print()



def beg():
    print ('You walk over to Roosevelt by the highway offramp, your feet hurt becuase your shoes are worn out')
    # print ('You Lose 1 energy')
    move()

def move():
    global currentLocation
    global timeOfDay
        # print(currentLocation) to test if the current locatino is accurate
    print ('Where do you want to go?')
    for i in range(len(places)):
        print('[',str(i+1),']',places[i],end=' ')
    goTo=input()
    if goTo == str(1):
        currentLocation=places[int(goTo)-1]
        park()
    elif goTo == str(2):
        currentLocation=places[int(goTo)-1]
        highway()
    elif goTo == str(3):
        currentLocation=places[int(goTo)-1]
        tent()
    elif goTo == str(4):
        currentLocation=places[int(goTo)-1]
        panera()
    elif goTo == str(5):
        currentLocation=places[int(goTo)-1]
        lake()
    elif goTo == str(6):
        currentLocation=places[int(goTo)-1]
        uptown()
        
    
    
       

def wake():
    # todaysWake=random.randint(1,2)
    # print('Test: Todays wake')
    print ('You wake up in your tent to the sound of an engine braking on the Dan Ryan headed west bound')
    move()
def park():
    print('You are at the park.')
    move()
def highway():
    print('You are at the highway offramp.')
    move()
def tent():
    global currentTimeOfDay
    global timeOfDay
    if currentTimeOfDay == timeOfDay[1]:
        print('You wake up to the sound of morning traffic and the drunkin ramblings of your neighbor')
        print('What do you want to do?')    
    else:
        print('You are at your tent, what do you want to do?')
        
    tentDo = ['Eat','Sleep','Leave']
    #To do @ tent: Eat Sleep Leave
    
    for i in range(len(tentDo)):
        print('[',str(i+1),']',tentDo[i],end=' ')
    doThis=input()
    if doThis == str(1):
        print('you eat')
    elif doThis == str(2):
        print('You sleep')
    elif doThis == str(3):
        print('You decide to take a hike')
        move()
    # elif doThis == str(4):
    # elif doThis == str(5):
    # elif doThis == str(6):
    
    print('You are at your tent.')
    move()
def panera():
    print('You are at Panera.')
    move()
def lake():
    print('You are at the lake.')
    move()
def uptown():
    print('You are at in Uptown.')
    move()
tent()

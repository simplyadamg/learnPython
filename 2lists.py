import random
love = [['days','weeks','months','years'],[4,1,6,1]]

# print(love[random.randint(0,3)][random.randint(0,3)])
for i in range(1,10):
    print(love[random.randint(0,1)][random.randint(0,3)])

# Sliced
spam = ['rat','cat','dog','monkey','rabbit','goldfish','lemur']
print('this is how a slice works')
print(spam[0:]) #all the items in the list
print(spam[:3]) #prints the first 3 items in the list
print(len(spam))
del spam[1]
print (len(spam))
print('rabbit' in spam) #is a value in a list
print('lion' not in spam) #checks if a value is absent from a list
print('lion' in spam) #is a value in a list
print('rabbit' not in spam) #checks if a value is absent from a list
#you can convert a value to a list by passing it to the list function
iQuit = 'Quit Job'
print(iQuit)
listJob =list(iQuit)
print(listJob)
# for i in range (1,10):
#     for j in range (0,len(listJob-1)):
#         print(listJob[j])

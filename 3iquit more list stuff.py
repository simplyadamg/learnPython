print('What do you want to say to your boss?')
iQuitNoList = input()
iQuitList = list(iQuitNoList)
leniQuitList = len(iQuitList)
for i in range (1,100):
    for j in range (0,leniQuitList):
        print(iQuitList[j],end="")
        if j == leniQuitList-1:
            print('',end=" ")
for i in iQuitList:
    print(i)

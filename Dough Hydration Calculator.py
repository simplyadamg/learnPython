def hydrartionCalc():
    print('This a dough hydration calcuator')
    print('Quantity flour in starter:')
    starterF = input()
    print('Quantity water in starter:')
    starterW = input()
    print('Quantity flour in main dough:')
    doughF = input()
    print('Quantity water in main dough:')
    doughW = input()
    finalHydration = (int(starterW)+int(doughW))/(int(starterF)+int(doughF))
    print('Your dough will have a final hydration of:')
    print(str(100 * round(finalHydration,2))+'%')
hydrartionCalc()  
import random

def printState(st):
    print("---------------------")
    for row in st:
        for col in row:
            print(col, end = "\t")
        print()
    print("---------------------")
    
def isGoal(st):
    goal = True
    for row in st:
        for col in row:
            if col == "Dirty":
                goal = False
                return goal
    return goal
    
def dirtifyState(st):
    for count in range(5):            
        row = random.randint(0,2)
        col = random.randint(0,2)
    
        st[row][col] = 'Dirty'

start_state = [['Clean','Clean','Clean'],
               ['Clean','Clean','Clean'],
               ['Clean','Clean','Clean']]
               
printState(start_state)
  


if isGoal(start_state):
    print("The goal has been reached")
else:
    print("The surface is still dirty!")

dirtifyState(start_state)
    
vac_x = random.randint(0,2)
vac_y = random.randint(0,2)

start_state[vac_x][vac_y] = start_state[vac_x][vac_y] + "*"
    
printState(start_state)

if isGoal(start_state):
    print("The goal has been reached")
else:
    print("The surface is still dirty!")
    

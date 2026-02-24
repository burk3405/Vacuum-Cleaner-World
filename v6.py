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
        
def reportGoal(st):
    if isGoal(start_state):
        print("The goal has been reached")
    else:
        print("The surface is still dirty!")
        
    

start_state = [['Clean','Clean','Clean'],
               ['Clean','Clean','Clean'],
               ['Clean','Clean','Clean']]
               
printState(start_state)
  


dirtifyState(start_state)
    
vac_x = random.randint(0,2)
vac_y = random.randint(0,2)

print("Vacuum is at", vac_x, vac_y)

start_state[vac_x][vac_y] = start_state[vac_x][vac_y] + "*"
    
printState(start_state)

reportGoal(start_state)
    
actions = "udlrs" # up, down, left, right, suck

next_action = random.choice(actions) # random movement! not ideal at all
print(next_action)

if next_action == 'u' and vac_y > 0:
    start_state[vac_x][vac_y] = start_state[vac_x][vac_y][0:5]
    vac_y -= 1
    start_state[vac_x][vac_y] = start_state[vac_x][vac_y] + "*"
    
elif next_action == 'd' and vac_y < 2:
    start_state[vac_x][vac_y] = start_state[vac_x][vac_y][0:5]
    vac_y += 1
    start_state[vac_x][vac_y] = start_state[vac_x][vac_y] + "*"
   
elif next_action == 'l' and vac_x > 0:
    start_state[vac_x][vac_y] = start_state[vac_x][vac_y][0:5]
    vac_x -= 1
    start_state[vac_x][vac_y] = start_state[vac_x][vac_y] + "*" 

elif next_action == 'r' and vac_x < 2:
    start_state[vac_x][vac_y] = start_state[vac_x][vac_y][0:5]
    vac_x += 1
    start_state[vac_x][vac_y] = start_state[vac_x][vac_y] + "*" 
    
elif next_action == 's':
    start_state[vac_x][vac_y] = start_state[vac_x][vac_y][0:5]
    
printState(start_state)
    

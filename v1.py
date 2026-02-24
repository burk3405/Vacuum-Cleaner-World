# Sample State at the beginning
#start_state = [['','',''],
#               ['','',''],
#               ['','','']]
  
import random

def printState(st):
    print("---------------------")
    for row in st:
        for col in row:
            print(col, end = "\t")
        print()
    print("---------------------")

start_state = [['Clean','Clean','Clean'],
               ['Clean','Clean','Clean'],
               ['Clean','Clean','Clean']]
               
printState(start_state)
  
for count in range(5):            
    row = random.randint(0,2)
    col = random.randint(0,2)
    
    start_state[row][col] = 'Dirty'
    
printState(start_state)

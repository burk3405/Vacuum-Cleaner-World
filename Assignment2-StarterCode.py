import copy
 
state = {
    "board": [[0,0,0],
              [0,0,0],
              [0,1,0]],
    "vac": [0,0], # [row,col]
    "preActions": []
}
 
# actions up down right left suck
actions = ['u','d','r','l','s']
 
def isGoal(st):
    for row in st["board"]:
        for col in row:
            if col == 1:
                return False
    return True
 
 
def makeChild(st,act):
    newSt = copy.deepcopy(st)
    if (act == 'l' and st["vac"][1]>0):
        newSt["vac"][1] -= 1
        newSt["preActions"].append('Left')
       
    if (act == 'r' and st["vac"][1]<2):
        newSt["vac"][1] += 1
        newSt["preActions"].append('Right')
       
    if (act == 'u' and st["vac"][0]>0):
        newSt["vac"][0] -= 1
        newSt["preActions"].append('Up')
       
    if (act == 'd' and st["vac"][0]<2):
        newSt["vac"][0] += 1
        newSt["preActions"].append('Down')
       
    if (act == 's'):
        newSt["board"][newSt["vac"][0]][newSt["vac"][1]] = 0
        newSt["preActions"].append('Suck')
 
    return newSt
       
 
bfsQueue = [];
bfsQueue.append(state)
 
while (len(bfsQueue)>0):
    st = bfsQueue.pop(0)
   
    if isGoal(st):
        print("Found!")
        print(st["preActions"])
        break
   
    for act in actions:
        bfsQueue.append(makeChild(st,act))

 

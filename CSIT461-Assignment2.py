# CSIT 461- Intro to AI/Knowledge Engineering
# Shahin Mehdipour Ataee
# SUNY Fredonia
# Spring 2026

# Assignment #2- 3x3 Vacuum Cleaner World: Search Algorithms
# Aaron Burkett
# 2/26/2026


import copy
import heapq

initialState = {
    "board": [[1,0,0],
              [0,0,1],
              [0,1,1]],
    "vac": [1,1], # [row, col]
    "preActions": [],
    "cost": 0
    }
    
visited = []

actionCost = {
    'u': 1,
    'd': 1,
    'l': 1,
    'r': 1,
    's': 1 # this cost can be changed in the future
}

# for graph-search
def encode(st): 
        code = ""
        for row in st["board"]:
            for col in row:
                code += str(col)
        code += str(st["vac"][0])
        code += str(st["vac"][1])
        return code


# actions up down left right suck
actions = ['u', 'd', 'l', 'r', 's']



def isGoal(st):
    for row in st["board"]:
            for col in row:
                if col ==1:
                        return False
    return True
 
    
def makeChild(st,act):
        newSt = copy.deepcopy(st)
        
        moved = False
        
        if (act == 'l' and st["vac"][1]>0):
            newSt["vac"][1] -= 1
            newSt["preActions"].append('Left')
            moved = True
            
        elif (act == 'r' and st["vac"][1]<2):
            newSt["vac"][1] += 1
            newSt["preActions"].append('Right')
            moved = True
        
        elif (act == 'u' and st["vac"][0]>0):
            newSt["vac"][0] -= 1
            newSt["preActions"].append('Up')
            moved = True
        
        elif (act == 'd' and st["vac"][0]<2):
            newSt["vac"][0] += 1
            newSt["preActions"].append('Down')
            moved = True
            
        elif (act == 's'):
            r, c = newSt["vac"]
            if newSt["board"][r][c] == 1:
                newSt["board"][r][c] = 0
                newSt["preActions"].append('Suck')
                moved = True
            else:
                return None   # prevent useless suck and program timeout
        
        if not moved:
            return None
        
        newSt["cost"] = st["cost"] + actionCost[act]
        
        return newSt

# BFS Queue Implementation-

print("Starting BFS Queue...")
state = copy.deepcopy(initialState)
bfsQueue = [state]
visited = [encode(state)]
found = False

while bfsQueue:
    st = bfsQueue.pop(0)

    if isGoal(st):
        print("BFS Found!")
        print(st["preActions"])
        found = True
        break

    for act in actions:
        child = makeChild(st, act)
        if child is None: continue
        en = encode(child)
        if en not in visited:
            bfsQueue.append(child)
            visited.append(en)

if not found:
    print("BFS Failed.")

# DFS Queue is the same, just pop last one instead of 0:

print("\nStarting DFS Stack...")
state = copy.deepcopy(initialState)
dfsQueue = [state]
visited = [encode(state)]
found = False

while dfsQueue:
    st = dfsQueue.pop()

    if isGoal(st):
        print("DFS Found!")
        print(st["preActions"])
        found = True
        break

    for act in actions:
        child = makeChild(st, act)
        if child is None: continue
        en = encode(child)
        if en not in visited:
            dfsQueue.append(child)
            visited.append(en)

if not found:
    print("DFS Failed.")

# UCS Implementation- Graph Search:

print("\nStarting UCS Graph Search...")
state = copy.deepcopy(initialState)
ucsQueue = []
counter = 0
bestCost = {}

heapq.heappush(ucsQueue, (state["cost"], counter, state))
bestCost[encode(state)] = 0
found = False

while ucsQueue:
    cost, _, st = heapq.heappop(ucsQueue)

    if isGoal(st):
        print("UCS Graph Found!")
        print("Cost:", st["cost"])
        print(st["preActions"])
        found = True
        break

    for act in actions:
        child = makeChild(st, act)
        if child is None: continue
        en = encode(child)

        if en not in bestCost or child["cost"] < bestCost[en]:
            bestCost[en] = child["cost"]
            counter += 1
            heapq.heappush(ucsQueue, (child["cost"], counter, child))

if not found:
    print("UCS Graph Failed.")

# UCS Implementation- Tree Search- allows for node revisitation:

print("\nStarting UCS Tree Search...")
state = copy.deepcopy(initialState)
ucsQueue = []
counter = 0

heapq.heappush(ucsQueue, (state["cost"], counter, state))
found = False

while ucsQueue:
    cost, _, st = heapq.heappop(ucsQueue)

    if isGoal(st):
        print("UCS Tree Found!")
        print("Cost:", st["cost"])
        print(st["preActions"])
        found = True
        break

    for act in actions:
        child = makeChild(st, act)
        if child is None: continue
        counter += 1
        heapq.heappush(ucsQueue, (child["cost"], counter, child))

if not found:
    print("UCS Tree Failed.")

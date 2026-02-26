import copy
import heapq

state = {
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
    's': 1
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
            
        newSt["cost"] = st["cost"] + actionCost[act]
        
        return newSt


bfsQueue = [];
bfsQueue.append(state)
visited = []
visited.append(encode(state))

while (len(bfsQueue)>0):
    st = bfsQueue.pop(0)
    
    if isGoal(st):
        print("Found!")
        print(st["preActions"])
        break
    
    for act in actions:
        child = makeChild(st,act)
        en_child = encode(child)
        if (not (en_child in visited)):
            bfsQueue.append(child)
            visited.append(en_child)


# DFS QUEUE is the same, just pop last one instead of 0.
dfsQueue = [];
dfsQueue.append(state)
visited = []
visited.append(encode(state))

while (len(dfsQueue) > 0):
    st = dfsQueue.pop()
    
    if isGoal(st):
        print("Found!")
        print(st["preActions"])
        break
    
    for act in actions:
        child = makeChild(st,act)
        en_child = encode(child)
        if not (en_child in visited):
            dfsQueue.append(child)
            visited.append(en_child)


# UCS Implementation- Tree Search- allows for node revisitation

ucsQueue = []
counter = 0

heapq.heappush(ucsQueue, (state["cost"], counter, state))

while (len(ucsQueue) > 0):
    
    cost, _, st = heapq.heappop(ucsQueue)
    
    if isGoal(st):
        print("Found!")
        print("Cost:", st["cost"])
        print(st["preActions"])
        break

    for act in actions:
        child = makeChild(st,act)
        counter += 1
        heapq.heappush(ucsQueue, (child["cost"], counter, child))
        
# UCS Implementation- Graph Search-

ucsQueue = []
counter = 0

bestCost = {}

heapq.heappush(ucsQueue, (state["cost"], counter, state))
bestCost[encode(state)] = 0

while (len(ucsQueue) > 0):
    
    cost, _, st = heapq.heappop(ucsQueue)
    
    if isGoal(st):
        print("Found! (UCS Graph Search)")
        print("Cost:", st["cost"])
        print(st["preActions"])
        break

    for act in actions:
        child = makeChild(st,act)
        en_child = encode(child)
        
        # If never seen OR found cheaper path
        if (en_child not in bestCost) or (child["cost"] < bestCost[en_child]):
            
            bestCost[en_child] = child["cost"]
            counter += 1
            heapq.heappush(ucsQueue, (child["cost"], counter, child))

# for A*, introduce the cost + a heuristic function. for every state, calcualte a heuristic gvalue and use that to pop. 

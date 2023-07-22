#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [HARSHA VALIVETI hvalivet]
#
# Based on skeleton code in CSCI B551, Fall 2021.
import sys
# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    a=house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]
    #print(printable_house_map(a))
    return a
    
#generating successors based on the house map,
# checking diagonally, row and column
def successors(house_map):
    a=[]
    lr=len(house_map)
    lc=len(house_map[0])
    #storing point as true
    point = True
    
    for r in range(lr):
        for c in range(lc):
            point = True
            if house_map[r][c] == '.':
                #left up
                for i,j in zip(range(r-1,-1,-1),range(c-1,-1,-1)):
                    
                        if house_map[i][j] == 'p':
                            #add false
                            point = False
                            break
                        if house_map[i][j] == 'X':
                            break
                        if house_map[r][j] == '@':
                            break
                #left down
                for i,j in zip(range(r+1,lr,1),range(c-1,-1,-1)):
                    
                        if house_map[i][j] == 'p':
                            #add false
                            point = False
                            break
                        if house_map[i][j] == 'X':
                            break
                        if house_map[r][j] == '@':
                            break
                #right up
                for i,j in zip(range(r-1,-1,-1),range(c+1,lc,1)):
                    
                        if house_map[i][j] == 'p':
                            #add false
                            point = False
                            break
                        if house_map[i][j] == 'X':
                            break
                        if house_map[r][j] == '@':
                            break
                #right down
                for i,j in zip(range(r+1,lr,1),range(c+1,lc,1)):
                    
                        if house_map[i][j] == 'p':
                            #add false
                            point = False
                            break
                        if house_map[i][j] == 'X':
                            break
                        if house_map[r][j] == '@':
                            break
                #row up
                for i in range(r-1,-1,-1):
                    
                        if house_map[i][c] == 'p':
                            #add false
                            point = False
                            break
                        if house_map[i][c] == 'X':
                            break
                        if house_map[r][j] == '@':
                            break
                #row down
                for i in range(r+1,lr,1):
                    
                        if house_map[i][c] == 'p':
                            #add false
                            point = False
                            break
                        if house_map[i][c] == 'X':
                            break
                        if house_map[r][j] == '@':
                            break
                #col left
                for j in range(c-1,-1,-1):
                    
                        if house_map[r][j] == 'p':
                            #add false
                            point = False
                            break
                        if house_map[r][j] == 'X':
                            break
                        if house_map[r][j] == '@':
                            break
                #col right
                for j in range(c+1,lc,1):
                    
                        if house_map[r][j] == 'p':
                            #add false
                            point = False
                            break
                        if house_map[r][j] == 'X':
                            break
                        if house_map[r][j] == '@':
                            break
                #checking point if it has encountered any pichu's
                if (point):
                    a.append(add_pichu(house_map, r, c))
    
    return a
    #pass
    #return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if house_map[r][c] == '.' ]

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map,k):
    fringe = [initial_house_map]
    while len(fringe) > 0:
        for new_house_map in successors( fringe.pop() ):
            if is_goal(new_house_map,k):
                return(new_house_map,True)
            fringe.append(new_house_map)
            
    #return false if it didn't find a solution by checking length of fringe
    if len(fringe) == 0:
        return(0,False)
# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")


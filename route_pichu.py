#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [HARSHA VALIVETI hvalivet]
#
# Based on skeleton code provided in CSCI B551, Fall 2021.

import sys
# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return (0 <= pos[0] < n)  and (0 <= pos[1] < m)

# Find the possible moves from position (row, col) UUURRDDDRRUURRDD
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))
        
        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@") ]


# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

def search(house_map):
        # Find pichu start position
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        #storing visited position as 1's and unvisited as 0's 
        visited = [[0] * len(house_map[0]) for _ in range(len(house_map[1]))]
        #path to store the directions taken by each position
        path=""
        fringe=[(pichu_loc,0,path)] # fringe stores the location, distance and its path
        parents={pichu_loc:(0,0)}
        while len(fringe) > 0:
                #popping the elements from fringe
                (curr_move, curr_dist,path)=fringe.pop()
                p=parents[curr_move]  #getting a parent from its position from dictionary
                #calculating moves for children from parent position
                x2 = -p[0] + curr_move[0]
                y2 = -p[1] + curr_move[1]
                
                #storing the moves based on parent and child position
                if x2 == 1 and y2 == 0:
                    path+="D"
                elif x2 == -1 and y2 == 0:
                    path+="U"
                elif x2 == 0 and y2 == -1:
                    path+="L"
                elif x2 == 0 and y2 == 1 :
                    path+="R"
                    
                #finding goal state and returning its distance    
                if house_map[curr_move[0]][curr_move[1]]=="@":
                    return (curr_dist,path)
                
                visited[curr_move[0]][curr_move[1]]=1 #marking the list when a position is visited
                
                for move in moves(house_map, *curr_move): #traversing through the valid moves from a current node
                
                    if visited[move[0]][move[1]] == 0:
                        parents[move]=curr_move #assigning valid move to its parent
                        
                        fringe.append((move, curr_dist + 1,path)) #appending into the fringe with move and its distance
                        fringe.sort(key = lambda x: x[1],reverse=True) #sorting the fringe based on the minimum distance at last
        
        if len(fringe) == 0:
                return (-1,"")
                    

# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + solution[1])

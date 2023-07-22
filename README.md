# Route Pichu (part-1) 

# Problem statement:

The map consists of N lines and M columns. Each cell of the house is marked with one of four symbols: 'p'. represents the agent’s current location, 'X' represents a wall through which the agent cannot pass, '.' represents open space over which the agent can fly, and '@' represents your location(person).

Points to be noted here is,

-A pichu can only pass through the '.'

-it cannot travel through a wall 'X'

-pichu has to reach the person '@'


# Initial state:

The given House_Map contains a pichu already placed, and it is considered as the initial state.

# State space:

A pichu can travel only through the open space '.' that reaches the person '@'

# Successor function:

The space to travel or move further by pichu is considerd as successor function

# Goal state:

Finding a shortest path to reach the person, if so return the path and distance, or -1

# Cost Function:

The cost of reaching the person through open space, each move considered as a unit of cost.

# Major changes made to the original code are,

-marking the visited ones, eliminates revisiting the explored positions

-modifying the fringe to keep the lowest distance at last, to get the least disctance to the goal state

-tracking parents to the moves

-directions of the path taken

```
pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        #storing visited position as 1's and unvisited as 0's 
        visited = [[0] * len(house_map[0]) for _ in range(len(house_map[1]))]
        #path to store the directions taken by each position
        path=""
        fringe=[(pichu_loc,0,path)] # fringe stores the location, distance and its path
        parents={pichu_loc:(0,0)}
```

# Challenges:

The main challenge here I found is, maintaining a list that has an ordered elements of position based on their distance from initial or starting point. I made the fringe such that, whenever it appends a position to it, i immediately sorted the list by taking distance of each in descending order.

```
fringe.sort(key = lambda x: x[1],reverse=True) #sorting the fringe based on the minimum distance at last
```

The code runs with main function,

-it takes the input file and parses them as House_Map, which contains the position of pichu,wall, and person.

-then it calls the 'Solve' function by giving an argument of House_Map

-First we have to identify the pichu location and store it in the 'Fringe' which is used as a space to store the tuple of
location, distance and its path(which i have taken to track the moves of a pichu). It immediately tries to explore the latest move it found
and generates the path from it.

-initialised a visited list to track the position by marking it as 1-visited and 0-unvisited, which prevents visiting
multiple times.

-Tracking parents(Dict) of a position to easily come back if there is no solution found

-It iterates over the fringe, up to its empty:

	-Poping from the fringe gives the current position, current distance and path of location

	-Calculating the moves based on the parent and its child position(Down, Up, Left, Right)
	
	-checks each time in advance if it founds a goal state or not, if finds, returns the distance and its path, then marking the visited position
	
	-iterating over the list generated from the 'Moves' function by taking current position and House_Map
	
	-assigning the generated list to the parent of current position, then appending the move to the fringe and sorting the fringe by having the lowest distance 1st.

-finally, checks for the length of Fringe for exhaustion, if so, it returns, -1 which means it doesn't find a solution

# Arrange Pichus (Part-2)

# Problem statement:

The map consists of N lines and M columns. Each cell of the house is marked with one of four symbols: 'p'. represents the agent pichu, 'X' represents a wall, '.' represents open space, and '@' represents your location(person). Placing the K agents in the Map such that, they have to be positioned such that no two agents can see one another. 

Points to be noted here is:

- A pichu may see other at when it is placed in the same row, column and diagonal. This can be avoided by placing the other pichu in b/w walls( X ) and person( @ )

- Majorly focuses on placing the given number of pichu's (K) which is goal state, rather than the distance compared to the 1st part.

- It can be placed only on spaces '.'

# State space:

Successive positions of placing the pichu's, such that it is not encountered by other pichu

# Initial state:

Here initial state can be any position in the House_Map, which has open space '.' only

# Goal state:

Placing the given number of pichu's (K) on the House_Map, if it is possible return "True" and printing the House_Map, or return "False"

# Successor function:

No pichu is seeing other pichu in the same,

	- Row
	
	- Column
	
	- Diagonal

But with the exception of placing pichus between a wall (X) and person ( @ ), which looks like " .pXp "

# Cost function:

Cost function for this is irrelevant, because its goal state is returning a True or False, whether it can place the given number of pichus or not.

# Major changes made to the original code are,

- Changing the successor function to not seeing pichu's each other ( no same row, column and Diagonal)

- if it finds a House_Map such that all pichus, return "True" and House_Map, or return "False"

# Challenges:

Generating the right successor function, such that no pichu's encounter each other. Approach used is same as N-queens model, checking diagonal, row and column for any pichu encounters. 


The code runs with main function,

-it takes the input, which contains the House_Map as file and a number of pichu's to be placed in the House_Map

-invokes the 'solve' function, which takes the House_Map and number of pichu's to be placed ( K ).

-inside this function,it tries to generate the successors from 'Successor' function based on the fringe.

	- the successor function is designed such a way that, it generates the positions, which no pichu's see each other.
	
	- no pichu is in same diagonal, row and column.
	
	- but the exception here it is, a pichu can be placed between a wall (X) or person ( @ )
	```
	pichu's to be placed is 7
	Starting from initial house map:
	....XXX
	.XXX...
	.......
	.X.X.X.
	.....XX
	p..X.@.

	Looking for solution...

	Here's what we found:
	.p..XXX
	.XXX.p.
	.......
	.X.X.Xp
	..p..XX
	p..Xp@p
	```
	
	- if the successor function finds a position to place the pichu, it adds the pichu to the House_Map and which returned house_map is added to the list.
	
	- this list is again returned to the 'solve' function to check if the House_Map has placed the given number of pichu's
	
	- if it has placed all the pichus, return House_Map and True.
	
	- if not found, return False, only by exploring all the successors present in the fringe.

# Conclusion:

This assignment helped me to understand the importance of right selection of successor function, maintaining the fringe that stores the prospective positions to explore, and most importantly having a good optimised code.

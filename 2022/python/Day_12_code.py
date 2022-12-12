import aocutils
import random

height_map = {}
current_height = 1
step_count = 0
input = aocutils.getAoCInput()
successful_walks = []
failed_walks = set()

def y_bounding(coord, height_map):
    if coord <= 0:
        coord = 0
    elif coord >= len(height_map[0])-1:
        coord = len(height_map[0])-1
    return(coord)

def x_bounding(coord, height_map):
    if coord <= 0:
        coord = 0
    elif coord >= len(height_map)-1: 
        coord = len(height_map)-1
    return(coord)

for row,line in enumerate(input):
        height_map[row] = []
        for col, char in enumerate(line.strip()):
            height = ord(char) - 96
            if height == -13:
                height = 1
                present_loc=start_loc = [row,col]
            elif height == -27:
                height = 26
                end_loc = [row,col]
            height_map[row].append(height)

while len(successful_walks) < 3:
    
    path_history = set()
    path_history.add(tuple(start_loc))
    step_count = 0
    present_loc = start_loc

    while present_loc != end_loc:
        moves_to_investigate = [(-1,0), (1,0), (0,-1), (0,1)] #up, down, left, right
        new_potential_coordinates = []
        uphill_moves = []
        current_height = height_map[present_loc[0]][present_loc[1]]

        for row, col in moves_to_investigate: # For each potential direction to go...
            row = x_bounding(present_loc[0]+row,height_map)
            col = y_bounding(present_loc[1]+col,height_map)
            coord_set = set()
            coord_set.add((row,col))
            if coord_set.issubset(path_history) == False and tuple(path_history.union(coord_set)) not in failed_walks:
                new_potential_coordinates.append([row,col]) #Figure out the coordinates

        if len(new_potential_coordinates) == 0:
            failed_walks.add(tuple(path_history))
            break
        
        for row, col in new_potential_coordinates:
            if  height_map[row][col] == current_height  \
                or height_map[row][col] == current_height+1:
                    uphill_moves.append([row,col])
        
        if len(uphill_moves) == 0:
            failed_walks.add(tuple(path_history))
            break

        present_loc = random.choice(uphill_moves)
        uphill_moves = []
        current_height = height_map[present_loc[0]][present_loc[1]]
        print("I decided to go to {}!".format(present_loc))
        path_history.add(tuple(present_loc))
        step_count += 1
        if present_loc == end_loc:
            successful_walks.append((step_count,path_history))

# for walk in successful_walks:
#     print("A run made it in {} steps and visiting {} ".format(walk[0],walk[1]))
# #print("Got to the end in {} steps following path {} !".format(step_count,path_history))
sorted(successful_walks)
print("The shortest run made it in {} steps and visiting {} ".format(successful_walks[-1][0],successful_walks[-1][1]))


        

            

import aocutils
import random
import time
import os
from copy import deepcopy

height_map = {}
current_height = 1
step_count = 0
input = aocutils.getAoCInput()
successful_walks = []
failed_walks = []
moves_to_investigate = [(0,1), (-1,0), (1,0), (0,-1)] #right, down, Up, left
visualise_walk = True

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

while len(successful_walks) < 1:

    if visualise_walk == True:
        visited_map = deepcopy(height_map)
    
    path_history = set()
    path_history.add(tuple(start_loc))
    step_count = 0
    present_loc = start_loc

    while present_loc != end_loc:
        new_potential_coordinates = []
        uphill_moves = []
        potential_path = []
        current_height = height_map[present_loc[0]][present_loc[1]]

        for row, col in moves_to_investigate: # For each potential direction to go...
            row = x_bounding(present_loc[0]+row,height_map)
            col = y_bounding(present_loc[1]+col,height_map)
            coord_set = set()
            coord_set.add((row,col))
            potential_path = path_history
            potential_path = potential_path.union(coord_set)
            if coord_set.issubset(path_history) == False and potential_path not in failed_walks:
                if abs(row-end_loc[0]) < abs(present_loc[0]-end_loc[0]):
                    new_potential_coordinates.insert(0,[row,col])
                    continue
                if abs(col-end_loc[1]) < abs(present_loc[1]-end_loc[1]):
                    new_potential_coordinates.insert(0,[row,col])
                    continue

                new_potential_coordinates.append([row,col]) #Figure out the coordinates

        if len(new_potential_coordinates) == 0:
            failed_walks.append(path_history)
            break
        
        for row, col in new_potential_coordinates:
            if  height_map[row][col] == current_height+1:
                    uphill_moves.insert(0,[row,col])
                    break
            elif height_map[row][col] == current_height:
                    uphill_moves.append([row,col])

        
        if len(uphill_moves) == 0:
            print("No valid climbing moves after {} steps!".format(step_count))
            failed_walks.append(path_history)
            break

        #present_loc = random.choice(uphill_moves)
        present_loc = uphill_moves[0]
        current_height = height_map[present_loc[0]][present_loc[1]]

        if visualise_walk == True:
            visited_map[present_loc[0]][present_loc[1]] = "+"
            for key, row in visited_map.items():
                letterrow = []
                thisRow = False
                destRow = False
                if key == present_loc[0]: thisRow = True
                if key == end_loc[0]: destRow = True
                for col, char in enumerate(row):
                    if thisRow and col == present_loc[1]:
                        letterrow.append("*")
                    if destRow and col == end_loc[1]:
                        letterrow.append("!")
                    elif isinstance(char,int):    
                        letterrow.append(chr(char+96))
                    else: letterrow.append(char)
                print("".join(letterrow))
            print("")
            time.sleep(0.05)
            os.system('cls' if os.name == 'nt' else 'clear')
        #print("I decided to go to {}!".format(present_loc))
        path_history.add(tuple(present_loc))
        step_count += 1
        if present_loc == end_loc:
            successful_walks.append((step_count,path_history))

# for walk in successful_walks:
#     print("A run made it in {} steps and visiting {} ".format(walk[0],walk[1]))
# #print("Got to the end in {} steps following path {} !".format(step_count,path_history))
sorted(successful_walks)
print("The shortest run made it in {} steps and visiting {} ".format(successful_walks[-1][0],successful_walks[-1][1]))


        

            

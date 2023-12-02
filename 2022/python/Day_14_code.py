import aocutils
import os
import time

sand_dropped = 0

lowest_col = 999
lowest_row = 999

highest_col = -1
highest_row = -1
sand_start = [500,0]
cave = {sand_start[1]: {sand_start[0]:'+'}}
current_coord = None


def lookAround(cave, sand_pos):

    square_D = [sand_pos[0], sand_pos[1]+1, cave[sand_pos[1]+1][sand_pos[0]]]
    square_D_L = [sand_pos[0]-1 ,sand_pos[1]+1, cave[sand_pos[1]+1][sand_pos[0]-1]]
    square_D_R = [sand_pos[0]+1, sand_pos[1]+1, cave[sand_pos[1]+1][sand_pos[0]+1]]
    square_L = [sand_pos[0]-1, sand_pos[1], cave[sand_pos[1]][sand_pos[0]-1]]

    return(square_D,square_D_L,square_D_R,square_L)

def validDestination(target_square):
    if target_square[2] != '#' and target_square[2] != 'o': return(True) #If space is free...
    else: return(False)

for row, text in enumerate(aocutils.getSplitAoCInput()):

    # print(text)
    # if first_col > int(text[0].split(',')[0]):
    #     first_col = int(text[0].split(',')[0])

    rock_paths = [x.strip() for x in text if x != '->']
    for rock in rock_paths:
        col = int(rock.split(',')[0])
        row = int(rock.split(',')[1])

        if col < lowest_col:
            lowest_col = col

        if row < lowest_row:
            lowest_row = row

        if col > highest_col:
            highest_col = col
        
        if row > highest_row:
            highest_row = row
        
        if current_coord is None: #If this is the first coord of the line...
            current_coord = [col,row] #Start here.
        else:
            if row != current_coord[1]:
                for _ in range(min(row,current_coord[1]),max(row,current_coord[1])+1):
                    if _ not in cave:
                        cave[_] = {}
                    cave[_][col] = '#'
            elif col != current_coord[0]: #If the column has changed, we're going along row dict keys
                for _ in range(min(col,current_coord[0]),max(col,current_coord[0])+1):
                    if row not in cave:
                        cave[row] = {}
                    cave[row][_] = '#'


        current_coord = [col,row]           


# Fill blank spaces in existing rows
for row, col in cave.items():
    for _ in range(lowest_col,highest_col+1):
        if _ not in cave[row]:
            cave[row][_] = '.' 

#Create missing rows to finish the square
for row in range(0, len(cave)+1):
    if row not in cave:
        cave.update({row: {x: '.' for x in range(lowest_col, highest_col+1)}})


while True:

    try:
        sand_pos = sand_start
        sand_dropped += 1
        while True:
            moved = False
            square_D, square_D_L, square_D_R, square_L = lookAround(cave,sand_pos)

            for square in [square_D,square_D_L,square_D_R]:
                if validDestination(square):
                    cave[sand_pos[1]][sand_pos[0]] = '.'
                    sand_pos = [square[0],square[1]]
                    cave[square[1]][square[0]] = 'o'
                    moved = True
                    break # Break this loop if this, else if it is a valid dest, break the while: true loop encasing

            if moved == False:
                break
                
                        

            # time.sleep(0.01)   
            # os.system('cls' if os.name == 'nt' else 'clear')
            # for row_num, row in sorted(cave.items()):
            #     sorted_list = []
            #     for _ in sorted(row.keys()):
            #         sorted_list += str(row[_])
                
            #     print(str(row_num) + " " + "".join(sorted_list))
    except KeyError:
        for row_num, row in sorted(cave.items()):
            sorted_list = []
            for _ in sorted(row.keys()):
                sorted_list += str(row[_])
            
            print(str(row_num) + " " + "".join(sorted_list))
        print("Fell off after {} sand grains!".format(sand_dropped-1)) #371 too low
        break
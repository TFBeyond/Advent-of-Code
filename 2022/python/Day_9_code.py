knot_list = [] #A list of lists stores the x and y of each knot.
num_of_knots = 10 #Easy to make it support an arbitrary number of knots, so why no-- Why shouldn't I?

#Sets handle filtering out duplicates for us.
pt1_visited_spots = set()
pt2_visited_spots = set()

#If a knot needs to go left or right, figure out which then push it one step in that direction
def close_x_distance(last_coords, knot_coords): 
            if last_coords[0] > knot_coords[0]:
                knot_coords[0] += 1
            elif last_coords[0] < knot_coords[0]:
                knot_coords[0] -= 1

# Same, but for up/down
def close_y_distance(last_coords, knot_coords):
            if last_coords[1] > knot_coords[1]:
                knot_coords[1] += 1
            elif last_coords[1] < knot_coords[1]:
                knot_coords[1] -= 1

close_in_the_distance = "Whispers~ falling silently, drift on the wind..."


def lets_implement_snake(knot_list, pt1_visited_spots, pt2_visited_spots): #...or ~= snake, at least.
    for knot_num, knot_coords in enumerate(knot_list[1:], start=1): # We never need to touch the head knot.

        last_coords = knot_list[knot_num-1] #This is why we start from 1. idx 0 - 1 makes idx -1, which is the _last_ element in the list.
        rope_x_distance=rope_y_distance = 0 #Track these individually to know whether to go in one axis or both axes.

        # distance is the difference between coordinates of the knot and the one further up the chain
        # abs shaves the + or - off to turn subtraction into difference.
        rope_x_distance += abs(last_coords[0] - knot_coords[0]) 
        rope_y_distance += abs(last_coords[1] - knot_coords[1])
        total_distance = rope_x_distance + rope_y_distance

        if total_distance > 2: #Do diagonal first if both axes need movement.
            close_x_distance(last_coords, knot_coords)
            close_y_distance(last_coords, knot_coords)
        elif rope_x_distance >= 2:
            close_x_distance(last_coords, knot_coords)
        elif rope_y_distance >= 2:
            close_y_distance(last_coords, knot_coords)

        knot_list[knot_num] = knot_coords
 
    pt1_visited_spots.add(tuple(knot_list[1]))
    pt2_visited_spots.add(tuple(knot_list[9]))
    return(knot_list)
        
for _ in range(num_of_knots): #Generate our arbitrary number of knots.
    knot_list.append([0,0])

with open("C:/Users/rob_k/Documents/advent_of_code/2022/inputs/Day_9_input.txt", 'r') as input:
    for line in input.readlines():
        line = line.strip().split(' ')
        instruction = line[0] #First split is the direction
        repeats = int(line[1]) #Second split is the number of steps

        for _ in range(repeats): #Move the head knot x steps...
            match instruction:
                case 'R': # ... to the right.
                    knot_list[0][0] += 1 # +1 to left/right!
                case 'U': # ... up.
                    knot_list[0][1] += 1 # +1 to up/down!
                case 'L': # ... to the left.
                    knot_list[0][0] -= 1 # -1 to left/right!
                case 'D': # ... down.
                    knot_list[0][1] -= 1 # -1 to up/down!

            #With the head knot moved, lets have everyone else catch up!
            knot_list = lets_implement_snake(knot_list, pt1_visited_spots, pt2_visited_spots)

print("The second knot in line went to {} different places. Golly!".format(len(pt1_visited_spots)))
print("Knot number {} went to {} different places. Wow!".format(num_of_knots, len(pt2_visited_spots)))
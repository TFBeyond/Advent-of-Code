visible_count = 0
max_score = 0
tree_map = {}

with open("C:/Users/rob_k/Documents/advent_of_code/Day_8_input.txt", 'r') as input:
    lines = input.readlines()
    for num,line in enumerate(lines):
        tree_map[str(num)] = []
        for char in line.strip():
            tree_map[str(num)].append(int(char))
    
for rowidx, row in enumerate(tree_map.values()):
    left_distance=up_distance=right_distance=down_distance = 0
    for colidx, tree in enumerate(row):

        column = [tree_map[i][colidx] for i in tree_map.keys()] #Weighty, oof.

        # if there's any taller to the left, right, top or bottom...
        if any(i >= tree for i in row[:colidx]) \
        and any(i >= tree for i in row[colidx+1:]) \
        and any(i >= tree for i in column[:rowidx]) \
        and any(i >= tree for i in column[rowidx+1:]):
            pass
        else: 
            visible_count += 1

        for other in reversed(row[:colidx]):
            left_distance += 1 # whatever happens, count the tree.
            if other >= tree: break #If it's equal or taller, line of sight is broken

        for other in row[colidx+1:]:
            right_distance += 1 # Whatever happens, count the tree!
            if other >= tree: break

        for other in reversed(column[:rowidx]):
            up_distance += 1 # WHATEVER HAPPENS, COUNT THE TREE!
            if other >= tree: break

        for other in column[rowidx+1:]:
            down_distance += 1 # COUNT. THE. TREE.
            if other >= tree: break 

        total_score = left_distance * up_distance * right_distance * down_distance
        konami_distance = up_distance*2 + down_distance*2 + left_distance + right_distance + left_distance + right_distance
        left_distance=up_distance=right_distance=down_distance = 0
        if total_score > max_score:
            max_score = total_score

print("The number of visible trees for pt1 is: {}".format(visible_count))
print("The maximum view score is: {}".format(max_score))
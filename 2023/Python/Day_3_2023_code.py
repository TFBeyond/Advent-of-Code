import aocutils
import re
input = aocutils.getSplitAoCInput()

    
coords_of_symbols = []
part_1_sum = 0
derp = "hi"
for line_num, line in enumerate(input):
    line = "".join(line).replace('.',' ')
    input[line_num] = line
    coords_of_symbols.append([])
    for i, char in enumerate(line):
        if (not char.isalnum() and not char.isspace()):
            coords_of_symbols[line_num].append(i)


def findFullNumber(string, starting_idx):

    num_start_idx=num_end_idx = starting_idx
    for neg_offset, char in reversed(list(enumerate(string[0:starting_idx]))):
        if char.isnumeric():
            num_start_idx = neg_offset
        else: break
    for pos_offset, char in enumerate(string[starting_idx:]):
        if char.isnumeric():
            num_end_idx = starting_idx + (pos_offset+1)
        else: break
    full_number = string[num_start_idx:num_end_idx]
    print("Full number is: {}!".format(full_number))
    return(int(full_number))

# print(coords_of_symbols)

for i,line in enumerate(coords_of_symbols):
     for coord in line:
        try: #Above checks
            if input[i-1][coord].isnumeric(): 
                number_to_add = findFullNumber(input[i-1], coord) # Up check
                print("Found full number {} on line {}".format(number_to_add, i))
                part_1_sum += number_to_add
            else: 
                if input[i-1][coord-1].isnumeric(): 
                    number_to_add = findFullNumber(input[i-1],coord-1) #Up-Left check
                    print("Found full number {} on line {}".format(number_to_add, i))
                    part_1_sum += number_to_add
                if input[i-1][coord+1].isnumeric(): 
                    number_to_add = findFullNumber(input[i-1],coord+1) #Up-Right check  
                    print("Found full number {} on line {}".format(number_to_add, i))
                    part_1_sum += number_to_add
        except: pass        
        try: #Below checks
            if input[i+1][coord].isnumeric():
                number_to_add = findFullNumber(input[i+1],coord) # Down check 
                print("Found full number {} on line {}".format(number_to_add, i+2))
                part_1_sum += number_to_add
            else: 
                if input[i+1][coord-1].isnumeric(): 
                    number_to_add = findFullNumber(input[i+1],coord-1) # Down-Left 
                    print("Found full number {} on line {}".format(number_to_add, i+2))
                    part_1_sum += number_to_add
                if input[i+1][coord+1].isnumeric(): 
                    number_to_add= findFullNumber(input[i+1],coord+1) # Down-Right 
                    print("Found full number {} on line {}".format(number_to_add, i+2))
                    part_1_sum += number_to_add
        except: pass
        try: # Left check
            if input[i][coord-1].isnumeric(): 
                number_to_add = findFullNumber(input[i],coord-1) #Left Check
                print("Found full number {} on line {}".format(number_to_add, i+1))
                part_1_sum += number_to_add
        except: pass
        try: # Right check
            if input[i][coord+1].isnumeric(): 
                number_to_add = findFullNumber(input[i],coord+1) # Right Check
                print("Found full number {} on line {}".format(number_to_add, i+1))
                part_1_sum += number_to_add                
        except: pass

print("Part 1 sum is: {}!".format(part_1_sum))



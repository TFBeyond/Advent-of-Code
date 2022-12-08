import string
import re
import copy

stack = [] #List of crate 'rows'
stacks_dict = {} #Dict of contents of each column
keys = {} #Key 'name' of each column.

inputMode = True #Start by considering input as initial stack diagram

with open("C:/Users/rob_k/Documents/advent_of_code/Day_5_input.txt", 'r') as input:
    current_line = input.readline() #Get initial line
    while current_line: #Until we run out of lines...
        if inputMode is True: #Have we parsed the initial stack setup?
            if current_line != '\n': #If we haven't hit the blank line separating initial stack from instructions...

                # Make final bit of string match the rest and get the 2nd of every 4 characters.
                # This matches both the box contents and the column numbers.
                stack.append([x for x in current_line.replace('\n',' ')[1::4]])
                current_line = input.readline() #Next line.
            else: #If we've finished  parsing the stack diagram...
                keys = [x.strip() for x in stack[-1]] #Get rid of whitespace from each column number.
                rows = stack[:-1] #Every row except the last is part of the box stack.

                for x in keys: # For every key
                    stacks_dict[x] = [] # make a blank list to store that column
                    for y in range(0,len(rows)): #For each row...
                        idx = int(x)-1 
                        stacks_dict[x] += rows[y][idx] #Add the box to its proper column in the dict.

                for k,v in stacks_dict.items():
                    stacks_dict[k] = [x for x in v if x != ' '] #Get rid of empty box spaces to prevent 'phantom' boxes.
                inputMode = False #Stop considering input as the stack diagram.
                pt2_stacks_dict = copy.deepcopy(stacks_dict) #Make exact duplicate of stacks_dict to modify for pt2
                current_line = input.readline() #Next line to hop over the blank line separator.

        else:
            instructions = re.findall('\W([0-9]*)\s?',current_line) #Get instructions as a list of numbers: 'Move x from y to z'
            grabbed_stack = [] #Contents of crane claw for pt2

            #pt1_operations. Could probably do something with reverse slicing here but eh.
            for _ in range(int(instructions[0])): 
               box = stacks_dict[instructions[1]].pop(0)
               stacks_dict[instructions[2]].insert(0,box)

            #pt2_operations
            grabbed_stack = pt2_stacks_dict[instructions[1]][:int(instructions[0])]
            del pt2_stacks_dict[instructions[1]][:int(instructions[0])]            
            pt2_stacks_dict[instructions[2]] = grabbed_stack + pt2_stacks_dict[instructions[2]]

            current_line = input.readline() #To the next line...

    for x in stacks_dict.values():
        print(x[0],end='') #pt1 answer
    
    print("\n") #Newline separates answers for legibility
    for x in pt2_stacks_dict.values():
        print(x[0],end='') #pt2 answer
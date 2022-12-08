from functools import reduce
import operator
import pprint
import copy

filesystem = {'/': {'total_size': 0}}
pwd = []
small_dirs = []
max_size = 70000000
required_size = 30000000
best_diff = None
dir_name = ''
dir_size = 0

def get_nested_key(dict_to_traverse,key_list): # Get to get to get to get to get...
    return reduce(operator.getitem, key_list,dict_to_traverse)

def set_nested_key(dataDict, key_list, value): # Get to get to get to get to get then set
    get_nested_key(dataDict, key_list[:-1])[key_list[-1]] = value

def parse_next_line(input): # Because defining functions looks neater
            current_line = input.readline()
            return(current_line.strip().split(' ')) # Fine I'll use split and not do some mad shit, jeez

def sum_values(target): #Recursively falls through a heap of directories and sums up their total_sizes
    for k, v in target.items():
        if isinstance(v, dict):
            dir_size = sum_values(v)
            #target['total_size'] += sum_values(v)
            target['total_size'] += dir_size
            if dir_size <= 100000:
                small_dirs.append(dir_size)
            
        elif k != 'total_size' and (isinstance(v, int) or v.isnumeric()):
            target['total_size'] += v
    return(target['total_size'])

def boldly_go(target,deficit): # Figures out how to address the deficit with the least effort or thought. Draw your own parallels.
    global best_diff
    global dir_name
    global dir_size

    for k, v in target.items():
        if isinstance(v, dict):
            boldly_go(v, deficit)
        elif k != 'total_size':
            if target['total_size'] > deficit:
                diff = target['total_size'] - deficit
                if best_diff is None or diff < best_diff:
                    best_diff = diff
                    dir_size = target['total_size']
                    dir_name = k
    return(dir_size, dir_name)

with open("C:/Users/rob_k/Documents/advent_of_code/Day_7_input.txt", 'r') as input:
    parsed_line = parse_next_line(input)
    while parsed_line:
        if parsed_line[0] == '$': #If it's a command...

            if parsed_line[1] == 'cd': # ...and if we're changing directories...
                if parsed_line[2] == '..': # ...and if we're going up... 
                    pwd.pop() # ...remove most recent chunk of the path
                    parsed_line = parse_next_line(input)
                else: # ...else, we're going deeper. Add it to the path.
                    pwd.append(parsed_line[2])
                    set_nested_key(filesystem,pwd + ['total_size'], 0)
                    parsed_line = parse_next_line(input)

            elif parsed_line[1] == 'ls': #If we're listing contents...
                try: # Have we been here already...?
                    get_nested_key(filesystem, pwd) # See if the path exists in filesystem dict
                except: #If not...
                    set_nested_key(filesystem, pwd, {}) #Create it

                parsed_line = parse_next_line(input)

                while parsed_line[0] != '$': # If it's NOT a command, it'll be the output of one.
                    if parsed_line[0] == 'dir': # Oh! We're describing a dir.
                        set_nested_key(filesystem,pwd + [parsed_line[1]], {}) # Put its name in the nightmare tree. 

                    elif parsed_line[0].isnumeric(): # Ooh, this is probably a filesize...
                        value = int(parsed_line[0])  # ints and strings don't mix for maths.
                        set_nested_key(filesystem,pwd + [parsed_line[1]], value) # Make a 'file'(key) with its size as the value.
                        set_nested_key(filesystem,pwd + ['total_size'], 0)
                    parsed_line = parse_next_line(input)
                    if parsed_line[0] == '': # In case your input file end with a blank line, break the loop.
                        break
        if parsed_line[0] == '': #Same here.
                        break

sum_values(filesystem['/']) # Do the thing to get the small things!
print("There are a lot of small directories on disk. Their sizes add up to {}. Isn't that neat?".format(sum(small_dirs)))

current_space = max_size - filesystem['/']['total_size'] # What do we have to work with, here?
space_deficit = required_size - current_space # Clean out your Shadowplay dir, -please-.
smallest_dir_size,smallest_dir_name = boldly_go(filesystem['/'],space_deficit) # Let me have this function name, that's all I ask

print("Currently the disk has {} space remaining, which means a deficit of {}! You could delete dir {} of size {}, maybe?".format(current_space,space_deficit,smallest_dir_name,smallest_dir_size))

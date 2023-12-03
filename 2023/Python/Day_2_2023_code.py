import aocutils

input = aocutils.getAoCInput()

cube_limits = {
    'red': {'max': 12, 'min': 999},
    'green': {'max': 13, 'min': 999},
    'blue': {'max': 14, 'min': 999}
}

id_tally = 0
power_tally = 0 
split_chars = [': ', ', ', '; ']

def validateCubes(id, line, cube_limits):
    game_possible = 'untested'
    cubes_found = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for clause in line:
        clause = clause.strip()
        num_of_cubes = clause.split(' ')[0]
        cubes_colour = clause.split(' ')[1]
        print("there are {} cubes of colour {}".format(num_of_cubes,cubes_colour))
        if int(num_of_cubes) > cubes_found[cubes_colour]:
            cubes_found[cubes_colour] = int(num_of_cubes)
        if int(num_of_cubes) > cube_limits[cubes_colour]['max']:
            print("game {} is IMPOSSIBLE.".format(id))
            game_possible = False

    if game_possible == 'untested':
        game_possible = True
        print("game {} is legit".format(id))
    results_dict = {
        'game_possible': game_possible,
        'min_red': cubes_found['red'],
        'min_green': cubes_found['green'],
        'min_blue': cubes_found['blue']
    }
    return(results_dict)


for i, line in enumerate(input):
    line = line.strip()
    line = line.split(': ')[1:]
    line = " ".join(line)
    line = line.split(', ')
    line = "; ".join(line)
    line = line.split(';')
    

    validate_results = validateCubes(i+1, line, cube_limits)
    if validate_results['game_possible'] == True:
        id_tally += i+1    
    power_of_min = validate_results['min_red'] * validate_results['min_green'] * validate_results['min_blue']
    power_tally += power_of_min
    print("There are least {} reds, {} greens and {} blues in Game {}".format(validate_results['min_red'], validate_results['min_green'], validate_results['min_blue'], i+1))

print("id_tally is: {}".format(id_tally))
print("power_tally is: {}".format(power_tally))


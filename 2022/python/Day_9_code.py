H_x=H_y=T_x=T_y = 0
visited_spots = set()

def tail_catchup_check(H_x,H_y,T_x,T_y):
    rope_distance = 0
    if H_x > T_x+1 or H_x < T_x-1:
        rope_distance += abs(H_x - T_x)

    if H_y > T_y+1 or H_y < T_y-1:
        rope_distance += abs(H_y - T_y)

    if rope_distance > 1:
        if H_x > T_x:
            T_x += 1
        elif H_x < T_x:
            T_x -= 1

        if H_y > T_y:
            T_y += 1
        elif H_y < T_y:
            T_y -= 1

    visited_spots.add((T_x,T_y))
    return(H_x,H_y,T_x,T_y)

with open("C:/Users/rob_k/Documents/advent_of_code/2022/inputs/Day_9_input.txt", 'r') as input:
    for line in input.readlines():
        line = line.strip().split(' ')
        instruction = line[0]
        repeats = int(line[1])

        match instruction:
            case 'R':
                for _ in range(repeats):
                    H_x += 1
                    H_x,H_y,T_x,T_y = tail_catchup_check(H_x,H_y,T_x,T_y)
            case 'U':
                for _ in range(repeats):
                    H_y += 1
                    H_x,H_y,T_x,T_y = tail_catchup_check(H_x,H_y,T_x,T_y)
            case 'L':
                for _ in range(repeats):
                    H_x -= 1
                    H_x,H_y,T_x,T_y = tail_catchup_check(H_x,H_y,T_x,T_y)
            case 'D':
                for _ in range(repeats):
                    H_y -= 1
                    H_x,H_y,T_x,T_y = tail_catchup_check(H_x,H_y,T_x,T_y)


    
print(len(visited_spots))
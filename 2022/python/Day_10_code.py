import aocutils
X = 1
record_cycle = 20
addition_queue = [0]
interesting_strengths = {}
interesting_cycles = [20,60,100,140,180,220]
total_strength = 0
screen = {}
for name in ["row_" + str(x) for x in range(1,7)]:
    screen.update({name: ['.' for x in range(40)]})


# Instructions can be queued. ex. 2: addx 3. 3: addx -4 results in the 3 being done at the end of cycle 3, THEN -4 starts
# execution in cycle 4, finishing after 5.
# Take note of the results during cycle 20, then every +40 after that. Multiply X by that cycle number to get number to add to result.

input = aocutils.getSplitAoCInput()
# for step, line in enumerate(input, start=1):
for line in input:
    if line[0] == 'noop':
        addition_queue.append(0)
    elif line[0] == 'addx':
        addition_queue.extend([0,line[1]])

for step, instruction in enumerate(addition_queue):

     #row number is the larger number between 1 and the ceiling of step ceil-divided by 40. This prevents div0 problems on cycle 0
    row_num = step // 40 + 1
 
    if step in interesting_cycles:
        interesting_strengths.update({record_cycle: X * step })
        record_cycle += 40
    X += int(addition_queue[step])

    bump = 40 * (row_num-1)
    
    if X>=0 and X <= 39:
        for n in [-1,0,1]:
           if X+bump+n == step:
                screen["row_"+str(row_num)][X+n] = "#"



for cycle, strength in interesting_strengths.items():
    print("At the end of cycle {}, the strength was {}".format(cycle, strength))
    total_strength += strength
print("Therefore, the sum of interesting strengths is {}!".format(total_strength))

for line in screen.values():
    print("".join(line))
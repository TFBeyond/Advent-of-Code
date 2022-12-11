import aocutils
import re
monkey_dict = {}
#monkey_num = 0
monkey_business = 0
input = aocutils.getSplitAoCInput()
round_count = 1
for line in input:
    match line[0]:
        case '':
            next
        case 'Monkey':
            monkey_num = line[1].replace(':','')
            monkey_dict[monkey_num] = {'inspected_count': 0}
        case 'Starting':
            monkey_dict[monkey_num]['inventory'] = [int(x.replace(',','')) for x in line[2:]] #Luckily no monkey starts empty-handed!
        case 'Operation:':
            monkey_dict[monkey_num]['operation'] = [line[-2],line[-1]]
        case 'Test:':
            monkey_dict[monkey_num]['test_divisor'] = int(line[-1])
        case 'If':
            if line[1] == 'true:':
                monkey_dict[monkey_num]['if_true_target'] = line[-1]
            elif line[1] == 'false:':
                monkey_dict[monkey_num]['if_false_target'] = line[-1]
            else:
                print("Uh-oh?")

while round_count <= 20:
    for mon_key, monkey_v in monkey_dict.items():
        for item in monkey_v['inventory'][:]:
            #print("Monkey {} is inspecting item {}".format(mon_key,item))
            monkey_v['inventory'].remove(item)
            # item = int(item)
            
            # First perform the operation
            if monkey_v['operation'][1] == 'old':
                second_arg = item
            else:
                second_arg = int(monkey_v['operation'][1])
            match monkey_v['operation'][0]:
                case '+':
                    item = item + second_arg
                case '*':
                    item = item * second_arg
                case '-':
                    item = item - second_arg
                case '/':
                    item = item / second_arg

            # Divide by floor(3) due to boredom
            item = item//3

            if item % monkey_v['test_divisor'] == 0:
                monkey_dict[monkey_v['if_true_target']]['inventory'].append(item)
                print("Monkey {} throws {} to {}".format(mon_key,item,monkey_v['if_true_target']))
            else: 
                monkey_dict[monkey_v['if_false_target']]['inventory'].append(item)
                print("Monkey {} throws {} to {}".format(mon_key,item,monkey_v['if_false_target']))
            monkey_v['inspected_count'] += 1
    round_count += 1

for mon_key, monkey_v in monkey_dict.items():
    print("Monkey {} has the following inventory: {}".format(mon_key, monkey_v['inventory']))
    print("Monkey {} has inspected {} items".format(mon_key, monkey_v['inspected_count']))

inspected_counts = [monkey_dict[i]['inspected_count'] for i in monkey_dict.keys()]
inspected_counts.sort()
monkey_business = inspected_counts[-2] * inspected_counts[-1]
print("Therefore, the level of monkey business is {}! Unacceptable!".format(monkey_business))
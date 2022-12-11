import aocutils

monkey_business = 0
monkey_dict = {}
divisor_product = 1
input = aocutils.getSplitAoCInput()

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
            divisor_product *= monkey_dict[monkey_num]['test_divisor']
            monkey_dict[monkey_num]['divisor_product'] = divisor_product

        case 'If':
            if line[1] == 'true:':
                monkey_dict[monkey_num]['if_true_target'] = line[-1]
            elif line[1] == 'false:':
                monkey_dict[monkey_num]['if_false_target'] = line[-1]

def monkeyGame(round_target, full_monkey_panic=True):
    for round_count in range(round_target):
        for monkey_v in monkey_dict.values():
            for item_worry_level in monkey_v['inventory'][:]:

                monkey_v['inventory'].remove(item_worry_level)
                
                if monkey_v['operation'][1] == 'old':
                    second_arg = item_worry_level
                else:
                    second_arg = int(monkey_v['operation'][1])
                match monkey_v['operation'][0]:
                    case '+':
                        item_worry_level += second_arg
                    case '*':
                        item_worry_level *= second_arg
                    case '-':
                        item_worry_level -= second_arg
                    case '/':
                        item_worry_level /= second_arg

                if full_monkey_panic == False:
                    item_worry_level //= 3

                if item_worry_level > divisor_product:
                    item_worry_level %= divisor_product

                #print("divisor product: {}, item before: {}, item after: {}".format(monkey_v['divisor_product'],before,item))

                if item_worry_level % monkey_v['test_divisor'] == 0:
                    monkey_dict[monkey_v['if_true_target']]['inventory'].append(item_worry_level)
                else: 
                    monkey_dict[monkey_v['if_false_target']]['inventory'].append(item_worry_level)
                monkey_v['inspected_count'] += 1

    for mon_key, monkey_v in monkey_dict.items():
        #print("Monkey {} has the following inventory: {}".format(mon_key, monkey_v['inventory']))
        print("Monkey {} has inspected {} items".format(mon_key, monkey_v['inspected_count']))

for pt, args in enumerate([[20, False],[10000,True]],start=1):
    monkeyGame(*args)
    inspected_counts = [monkey_dict[i]['inspected_count'] for i in monkey_dict.keys()]
    inspected_counts.sort()                                                                        
    monkey_business = inspected_counts[-2] * inspected_counts[-1]
    print("Therefore, the level of monkey business in part {} is {}! Unacceptable!\n".format(pt, monkey_business))
import aocutils
import json

def convert_to_list(x):
    if isinstance(x, int):
        x = [x]
    return(x)

def compare_ints(a,b):
    if a < b: 
        return(0)
    elif a > b:
        return(1)
    elif a == b:
        return(2)

def compare_lists(a,b):

    a = convert_to_list(a)
    b = convert_to_list(b)

    if len(a) <= len(b):
        length = len(b)
    elif len(b) < len(a):
        length = len(a)

    for _ in range(length):
        if _ >= len(a):
            return(0)
        if _ >= len(b):
            return(1)

        if isinstance(a[_],list) or isinstance(b[_],list):
            result = compare_lists(a[_],b[_])
        else:
            result = compare_ints(a[_],b[_])
        
        if result == 0:
            return(0)
        elif result == 1:
            return(1)

a=b = None
correct_pair_sum = 0
pair_index = 1
input = aocutils.getSplitAoCInput()
pairs_list = []

for line_num, line in enumerate(input):

    line = input[line_num]
    if line == ['']:
        continue
    elif a == None:
        a = json.loads(line[0])
        num_a = line_num+1
        continue
    elif b == None:
        b = json.loads(line[0])
        num_b = line_num+1
        result = compare_lists(a,b)
        if result == 0:
            correct_pair_sum += pair_index
            pairs_list.extend([a,b])
        elif result == 1:
            pairs_list.extend([b,a])
        result=a=b = None
        pair_index += 1
        continue


print("Pt1's answer is: {}".format(correct_pair_sum))

pairs_list.extend([[[2]],[[6]]])
i = 0
while i < len(pairs_list)-1:
    a = pairs_list[i]
    b = pairs_list[i+1]
    if a == [[2]]:
        first_divider_index = i+1
    if a == [[6]]:
        second_divider_index = i+1

    result = compare_lists(a,b)
    if result == 1:
        pairs_list[i] = b
        pairs_list[i+1] = a
        i = 0
    else: i += 1

print("Pt2 answer is {} * {} = {}".format(first_divider_index,second_divider_index,first_divider_index*second_divider_index))  
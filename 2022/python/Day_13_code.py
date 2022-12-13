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
    else:
        print("Oops?")

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

#Pair 1 + 2 + 3
# For a in left, compare to b in right. a = left[idx], b = right[idx] If a or b is list, compare each item to its counterpart. a[_] < or > b[_] if _ out of range, use -1 instead. If a < b, good. if b > a, bad. Else, continue. 
# good if left[idx] out of range, bad if right[idx] out of range.

a=b = None
correct_pair_sum = 0
pair_index = 1
input = aocutils.getSplitAoCInput()
for line_num, line in enumerate(input):
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
        print("After {}({}-{}), it is {}".format(pair_index, num_a, num_b, correct_pair_sum))
        result=a=b = None
        pair_index += 1
        continue

print(correct_pair_sum)
    
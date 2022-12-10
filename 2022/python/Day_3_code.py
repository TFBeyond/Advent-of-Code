import string
import aocutils

priority_mapping = {}
current_group = []
pt1_priority_total=pt2_priority_total = 0

# Set priority mapping
_ = 1
for char in string.ascii_lowercase + string.ascii_uppercase:
    priority_mapping[char] = _
    _ += 1

input = aocutils.getSplitAoCInput()
for line in input:
        line = line[0]
        current_group.append(set(line))

        # pt1 answer
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        for char in first_half:
            if char in second_half:
                pt1_priority_total += priority_mapping[char]               
                break

        # pt2 answer
        if len(current_group) == 3:
            common_letter = current_group[0].intersection(*current_group)
            pt2_priority_total += priority_mapping[common_letter.pop()]
            current_group = []

print("part 1 answer is: {}".format(pt1_priority_total))
print("part 2 answer is: {}".format(pt2_priority_total))
elf_dict = {}
elf_counter = 1
total = 0

with open("C:/Users/rob_k/Documents/advent_of_code/2022/inputs/Day_1_input.txt", 'r') as input:
    for x in input.readlines():
        if x != '\n':
            total += int(x)
        else: 
            elf_dict["elf_{}".format(elf_counter)] = total
            elf_counter += 1
            total = 0
key = max(elf_dict, key=elf_dict.get)

print("The elf with the largest supply is: {} with a value of: {}".format(key, elf_dict[key]))

top_three = {}
for _ in range(0,3):
    top_three["top_{}".format(_)] = elf_dict.pop(key)
    key = max(elf_dict, key=elf_dict.get)

print("The top three elves have a combined total of {}!".format(sum(top_three.values())))
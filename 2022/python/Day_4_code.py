subset_counter = 0
intersection_counter = 0
import aocutils

input = aocutils.getSplitAoCInput(",")

for elf_pair in input:

    elf_1_tasks = set(range(int(elf_pair[0].split("-")[0]),int(elf_pair[0].split("-")[1]) + 1))
    elf_2_tasks = set(range(int(elf_pair[1].split("-")[0]),int(elf_pair[1].split("-")[1]) + 1))

    if not elf_1_tasks.difference(elf_2_tasks): subset_counter += 1
    elif not elf_2_tasks.difference(elf_1_tasks): subset_counter += 1

    if elf_1_tasks.intersection(elf_2_tasks): intersection_counter += 1
    elif elf_1_tasks.intersection(elf_2_tasks): intersection_counter += 1

print("pt1 overlap counter is {}!".format(subset_counter))
print("pt2 intsersection counter is {}!".format(intersection_counter))
import aocutils

results_matrix = {
    "A": { # opp rock
        "X": 4, # my rock
        "Y": 8, # my paper
        "Z": 3  # my scissors
    },
    "B": { # opp paper
        "X": 1, # my rock
        "Y": 5, # my paper
        "Z": 9  # my scissors
    },
    "C": { # opp scissors
        "X": 7, # my rock
        "Y": 2, # my paper
        "Z": 6  # my scissors
    }
}

results_matrix_2 = {
    "A": { # opp rock
        "X": 3, # my loss (scissors) 0 + 3
        "Y": 4, # my draw (rock) 3 + 1
        "Z": 8  # my win (paper) 6 + 2
    },
    "B": { # opp paper
        "X": 1, # my loss (rock) 0 + 1
        "Y": 5, # my draw (paper) 3 + 2
        "Z": 9  # my win (scissors) 6 + 3
    },
    "C": { # opp scissors
        "X": 2, # my loss (paper) 0 + 2
        "Y": 6, # my draw (scissors) 3 + 3
        "Z": 7  # my win (rock) 6 + 1
    }
}

pt1_total=pt2_total = 0
line_counter = 1
input = aocutils.getSplitAoCInput()
for line in input:
    pt1_total += results_matrix[line[0]][line[1]]
    pt2_total += results_matrix_2[line[0]][line[1]]
    line_counter += 1

print("part 1's total is: {}".format(pt1_total))
print("part 2's total is: {}".format(pt2_total))

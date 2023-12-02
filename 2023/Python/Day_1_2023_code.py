import aocutils

input = aocutils.getSplitAoCInput()

word_to_num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
line_num = 0
count = 0
grabbed_numbers = []

for line in input:
    line_num += 1
    charstring = ''
    word_in_progress = ''
    for char in line[0]:
        if char.isalpha():
            word_in_progress += char
            for text_num in word_to_num_dict.keys():
                if text_num in word_in_progress:
                    charstring += word_to_num_dict[text_num]
                    word_in_progress = char
                    break
        if char.isdigit():
            charstring += char
            word_in_progress = ''


    if len(charstring) > 1:
        charstring = charstring[0] + charstring[-1]
    else: charstring += charstring
    grabbed_numbers.append(charstring)

for i, number in enumerate(grabbed_numbers):
    count += int(number)
    print("Line {} added {} to the cumulative count for a total of {}".format(i+1, number, count))


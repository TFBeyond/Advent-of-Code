with open("C:/Users/rob_k/Documents/advent_of_code/Day_6_input.txt", 'r') as input:
    line = input.readline()
    buffer = []
    packet_found = False
    for pos,char in enumerate(line, start=1):
        if char in buffer:
            while char in buffer:
                buffer.pop(0)
        buffer.append(char)
        
        if len(buffer) == 4 and packet_found == False:
            print("Buffer length 4 achieved at position {}".format(pos))
            packet_found = True
        if len(buffer) == 14:
            print("Buffer length 14 achieved at position {}".format(pos))
            break
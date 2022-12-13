def main(input):
    f = open(input, 'r')
    cycle = 0
    reg = 1

    reg_list = []
    for line in f:
        line = line.strip()
        if line == 'noop':
            cycle +=1
            if cycle <=220 and cycle % 40 == 20:
                reg_list.append(reg*cycle)
        else:
            line, num = line.split()
            cycle+=1
            if cycle <=220 and cycle % 40 == 20:
                reg_list.append(reg*cycle)
            cycle+=1
            if cycle <=220 and cycle % 40 == 20:
                reg_list.append(reg*cycle)
            reg += int(num)













main('inputday10')
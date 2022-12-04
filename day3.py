
#part 2
def main2(file):
    carrying = []
    f= open(file,'r')
    count=0
    i=0
    group = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for line in f:
        line = line.strip()
        group.append(set(line))
        if len(group)==3:
            inter =''.join(group[0].intersection(group[1]).intersection(group[2]))
            i+= alphabet.index(inter) +1
            group = []




    print(i)








main2('inputday3')









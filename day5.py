import queue


def main1(file):
    f = open(file, 'r')
    count = 0
    # part 2 solution
    word = ""
    crates = [['c', 's', 'b', 'g'], ['g', 'v', 'n', 'j', 'h', 'w', 'm', 'n', 't'], ['s', 'q', 'm'],
              ['m', 'n', 'w', 't', 'l', 's', 'b'], ['p', 'w', 'g', 'v', 't', 'f', 'z', 'j'],
              ['s', 'h', 'q', 'g', 'b', 't', 'c'], ['w', 'b', 'p', 'j', 't'], ['m', 'q', 't', 'f', 'z', 'c', 'd', 'g'],
              ['f', 'p', 'b', 'h', 's', 'n']]

    for i in range(len(crates)):
        crates[i].reverse()

    for line in f:
        line = line.strip()

        moves = [int(s) for s in line.split() if s.isdigit()]
        swap(moves[0], moves[1], moves[2], crates)


    for i in range(len(crates)):
        if (crates[i]):
            word += crates[i][-1].upper()
    print(word)


def swap(num, pos1, pos2, que):
    for i in range(num):
        if (que[pos1 - 1]):
            que[pos2 - 1].append(que[pos1 - 1].pop())


def main2(file):
    f = open(file, 'r')

    # part 2 solution
    word = ""
    crates = [['c', 's', 'b', 'g'], ['g', 'v', 'n', 'j', 'h', 'w', 'm', 'n', 't'], ['s', 'q', 'm'],
              ['m', 'n', 'w', 't', 'l', 's', 'b'], ['p', 'w', 'g', 'v', 't', 'f', 'z', 'j'],
              ['s', 'h', 'q', 'g', 'b', 't', 'c'], ['w', 'b', 'p', 'j', 't'], ['m', 'q', 't', 'f', 'z', 'c', 'd', 'g'],
              ['f', 'p', 'b', 'h', 's', 'n']]

    for i in range(len(crates)):
        crates[i].reverse()

    for line in f:
        line = line.strip()

        moves = [int(s) for s in line.split() if s.isdigit()]

        swap2(moves[0], moves[1], moves[2], crates)

    for i in range(len(crates)):
        if (crates[i]):
            word += crates[i][-1].upper()
    print(crates)
    print(word)


def swap2(num, pos1, pos2, que):
    temp = []
    for i in range(num):
        temp.append(que[pos1 - 1].pop())
    temp.reverse()

    que[pos2 - 1].extend(temp)





main2('inputday5')

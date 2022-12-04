# part 2 solution
def main1(file):
    f = open(file, 'r')
    count = 0
    # part 2 solution
    for line in f:
        line = line.strip()
        r1, r2 = line.split(',')
        n1, n2 = r1.split('-')
        p1, p2 = r2.split('-')
        if int(n1) in range(int(p1), int(p2) + 1) and int(n2) in range(int(p1), int(p2) + 1):
            count += 1
        elif int(p1) in range(int(n1), int(n2) + 1) and int(p2) in range(int(n1), int(n2) + 1):
            count += 1

    print(count)


# part 2 solution
def main2(file):
    f = open(file, 'r')
    count = 0

    for line in f:
        line = line.strip()
        r1, r2 = line.split(',')
        n1, n2 = r1.split('-')
        p1, p2 = r2.split('-')
        if int(n1) in range(int(p1), int(p2) + 1) or int(n2) in range(int(p1), int(p2) + 1):
            count += 1
        elif int(p1) in range(int(n1), int(n2) + 1) or int(p2) in range(int(n1), int(n2) + 1):
            count += 1

    print(count)


main1('inputday4')
main2('inputday4')

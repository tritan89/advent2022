def main(file):
    f = open(file, 'r')
    score = 0
    for line in f:
        line = line.strip()

        # A rock X lose
        # B paper Y draw
        # C scissors Z win
        score += trials2(line)
    print(score)

#part two solution
def trials2(rnd):

    match rnd:
        case 'A X':
            return 3
        case 'B X': #loss
            return 1
        case 'C X':
            return 2
        case 'A Y':#tie
            return 4
        case 'B Y':
            return 5
        case 'C Y':
            return 6
        case 'A Z':
            return 8
        case 'B Z':
            return 9
        case 'C Z':
            return 7


main('inputday2')

from collections import Counter
def check_flag():
    flag =""
    file = open('inputday6', 'r')
    count=0
    while 1:
        char = file.read(1)

        if not char:
            break
        count += 1
        flag += char
        #part one change 14 to 4
        if len(flag) > 14:
            flag = flag[1:]
        if uniqueCharacters(flag) and len(flag) == 14:
            print(count)
            break

    file.close()

def uniqueCharacters(s):
    return not any(filter(lambda x: x > 1, list(Counter(list(s)).values())))

check_flag()
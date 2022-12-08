import re

#part 1
def rechecks(cmd):
    if cmd == '$ cd ..':
        return 0
    elif cmd.__contains__('dir'):
        return [3, cmd[4:]]
    elif cmd.__contains__('$ cd '):  # change dir
        return [1, cmd[5:]]
    elif cmd == "$ ls":
        return 2
    else:
        cmd = cmd.split()
        return [4, cmd[0], cmd[1]]


def process(filename):
    f = open(filename, 'r')
    currdir = []
    dirlist = {}

    for line in f:
        line = line.strip()
        curr = rechecks(line)

        if curr == 0:  # go back
            currdir.pop()
        elif curr == 2:  # list files
            continue
        elif curr[0] == 1:  # change dir
            currdir.append(curr[1])

        elif curr[0] == 3:  # add dir
            #dirlist[curr[1]] = []
            continue
        elif curr[0] == 4:  # add files
            for i in range(1, len(currdir)+1):
                a = "/".join(currdir[:i])
                if a not in dirlist:
                    dirlist[a] = []
            #dirlist[currdir[-1]].append(int(curr[1]))
                dirlist[a].append(int(curr[1]))



    total_sum = 0
    for key, v in dirlist.items():
        dir_sum = sum(v)
        print(key, v, dir_sum)
        if dir_sum <= 100000:
            print(dir_sum)
            total_sum += dir_sum

    print(total_sum)




def process2(filename):
    f = open(filename, 'r')
    currdir = []
    dirlist = {}

    for line in f:
        line = line.strip()
        curr = rechecks(line)

        if curr == 0:  # go back
            currdir.pop()
        elif curr == 2:  # list files
            continue
        elif curr[0] == 1:  # change dir
            currdir.append(curr[1])

        elif curr[0] == 3:  # add dir
            #dirlist[curr[1]] = []
            continue
        elif curr[0] == 4:  # add files
            for i in range(1, len(currdir)+1):
                a = "/".join(currdir[:i])
                if a not in dirlist:
                    dirlist[a] = []
            #dirlist[currdir[-1]].append(int(curr[1]))
                dirlist[a].append(int(curr[1]))



    total = 70000000
    avail = total - 41035571
    need = 30000000 - avail
    vals =[]
    for key, v in dirlist.items():
        dir_sum = sum(v)
        print(key, v, dir_sum)
        if dir_sum >= need:
            vals.append(dir_sum)
    closest = min(vals, key= lambda x:abs(x-need))



    print(closest)

process2('inputday7')

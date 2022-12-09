def main(input):
    f = open(input, 'r')
    rows = []
    cols = [[] for i in range(99)]
    for line in f:
        line = line.strip()

        i = 0
        rows.append([int(x) for x in str(line)])
        for num in line:
            cols[i].append(int(num))
            i += 1
    visible = 0
    i = 1
    visible = set()
    for trees in rows[1:-1]:

        temp = check_vis_r(trees, i)

        for tree in temp:
            visible.add(tuple(tree))
        i += 1
    j = 1
    for trees in cols[1:-1]:
        temp= check_vis_c(trees, j)
        for tree in temp:
            visible.add(tuple(tree))
        j += 1

    edges = 4 * len(rows[0]) - 4

    print(edges)
    print(len(visible)+edges)


def check_vis_r(row, col):
    vis = 0
    indexs = []
    size = len(row)
    for i in range(1, size - 1):

        flag_r = 0
        flag_l = 0
        # check current index against everything to the right
        for j in row[i+1:]:
            if row[i] <= j:
                flag_r = 1
                break

        # check current index against everything to the left
        for j in row[: i]:
            if row[i] <= j:
                flag_l = 1
                break

        if flag_r!=1 or flag_l != 1:
            vis += 1

            indexs.append([i + 1, col + 1])
    print("rows", indexs)
    return indexs


def check_vis_c(row, col):
    vis = 0
    indexs = []
    size = len(row)
    for i in range(1, size - 1):

        flag_r = 0
        flag_l = 0
        # check current index against everything to the right
        for j in row[i+1:]:
            if row[i] <= j:
                flag_r = 1
                break

        # check current index against everything to the left
        for j in row[:i]:
            if row[i] <= j:
                flag_l = 1
                break

        if flag_r != 1 or flag_l != 1:
            vis += 1

            indexs.append([col + 1,i + 1])
    print("cols", indexs)
    return indexs

if __name__ == '__main__':
    main('inputday8')

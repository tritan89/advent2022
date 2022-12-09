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
    scores = []
    for i in range(99):
        for j in range(99):
            scores_r = vis_score_row(rows[i],j)
            scores_c = vis_score_col(cols[j], i)
            scores.append(scores_c*scores_r)
    print(max(scores))




def vis_score_row(row: list,  index):
    score_r = 0
    score_l = 0

    # check current index against everything to the right
    for j in row[index + 1:]:
        if row[index] > j:
            score_r += 1
        elif row[index] == j:
            score_r += 1
            break
        else:
            score_r += 1
            break
    print(row[index], score_r)
    # check current index against everything to the left
    l_list= row[:index]
    l_list.reverse()
    for k in l_list:
        if row[index] > k:
            score_l += 1
        elif row[index] == k:
            score_l += 1
            break

        else:
            score_l += 1
            break




    return  score_l * score_r

def vis_score_col( col: list, index):
    score_t = 0
    score_b = 0
  # check current index against everything to the TOP

    t_list = col[:index]
    t_list.reverse()
    #print(col[index],t_list)
    for l in t_list:

        if col[index] > l:
            score_t += 1
        elif col[index] == l:
            score_t += 1
            break
        else:
            score_t += 1
            break

    # check current index against everything to the bottom

    for m in col[index + 1:]:
        if col[index] > m:
            score_b += 1
        elif col[index] == m:
            score_b += 1
            break
        else:
            score_b += 1
            break

    return score_t * score_b


if __name__ == '__main__':
    main('inputday8')

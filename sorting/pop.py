ml = ["de", "cd", "ab", "dbz"]

l = len(ml)
for i in range(1, l, 1):
    ins_ind = i
    cur_val = ml.pop(i)
    for j in range(i - 1, -1, -1):
        if ml[j] < cur_val:
            ins_ind = j    
    ml.insert(ins_ind, cur_val)

    print(ml)
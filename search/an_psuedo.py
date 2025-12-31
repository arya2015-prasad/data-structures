def s(st, sub):
    
    if sub == "":
        return 0

    if st == "" and sub == "":
        return 0
    
    h = 0
    k = 0
    m = -1

    while (h < (len(st))) and (k < (len(sub))):
        if st(h) == sub[k]:
            h += 1
            k += 1
            if m == -1:
                m = h
        
        else:
            k = 0
            if m > 0:
                h = m
                m = -1
            
            else:
                h += 1
    
    if m > -1:
        return m - 1
    else:
        return -1
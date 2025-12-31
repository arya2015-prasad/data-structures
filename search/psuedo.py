def search(string, substring):
    
    if substring == "":
        return 0

    if string == "" and substring == "":
        return 0

    i = 0
    j = 0
    mi = -1

    while (i < (len(string))) and (j < (len(substring))):
        if string[i] == substring[j]:
            i += 1
            j += 1
            if mi == -1:
                mi = i
            
        else:
            j = 0
            if mi > 0:
                i = mi
                mi = -1
            else:
                i += 1
    
    if mi > -1:
        return mi - 1
    else:
        return -1
def ss(s, sb):
    if s == "" and sb == "":
        return 0

    if s == "":
        return 0
    
    r = 0
    t = 0
    mi = -1
    while (r < len(s)) and (t < len(sb)):
        if sb[t] == s[r]:
            r += 1
            t += 1
            if mi == -1:
                mi = r
        else:
            r = 0
            if mi > 0:
                r = mi
                mi = -1
            
            else:
                r += 1
                
    if mi > -1:
        return mi -1
    else:
        return -1

print(ss(s = "efgasgjiee", sb = "gji"))
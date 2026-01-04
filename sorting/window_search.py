def search(string, substr):
    d = len(substr)
    s = 0

    while s < len(string):
        sb = string[s : s + d]
        if substr == sb:
            return s
        else:
            s += 1
    return -1




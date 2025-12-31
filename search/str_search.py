## Function to perform subtring search on a string and find the given substring
## If the substring is found in the string, return the index of the substring else return -1
## @param string, the string in which the substring is to be searched for
## @param substring, the substring to be searched
## @return index of the substring found else -1
def substr(string, substring):

    if substring == "":
        return 0

    if string == "" and substring == "":
        return 0


    x = 0
    y = 0
    matchIndex = -1

    while x < len(string) and y < len(substring):
        if string[x] == substring[y]:
            y += 1
            x += 1
            if matchIndex == -1:
                matchIndex = x
        else:
            y = 0
            if matchIndex > 0:
                x = matchIndex
                matchIndex = -1
            else:
                x += 1
        
    if matchIndex > -1 :
        return matchIndex - 1
    else :
        return -1


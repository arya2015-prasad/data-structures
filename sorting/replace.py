from window_search import search
def rep(string, find, repe):
    index = search(string, find)
    if index >= 0:
         replacement = string[0 : index] + repe + string[index + len(find) : len(string)]
         return replacement
    
    else:
        return -1

print(rep("rtsesa44", "sa4", "dt"))
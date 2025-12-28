## Function to perform sequential search on an array and find the given element
## If the element is found in the array, return the index of the element else return -1
## @param arr, the array of elements
## @param num, the element to be searched
## @return index of the element found else -1
def search(arr, num):
    i = 0
    index = -1

    while (i < len(arr)):
        if num == arr[i]:
            index = i
            break
        i += 1
    
    return index

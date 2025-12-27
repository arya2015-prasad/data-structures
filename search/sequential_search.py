## Function to perform sequential search on an integer array and find a number
## If the number is found in the array, return the index of the number else return -1
## @param arr, the array of integers
## @param num, the number to be searched
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

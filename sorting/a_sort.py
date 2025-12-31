def swap(arr, i, j):
    c = arr[i]
    arr[i] = arr[j]
    arr[j] = c
    print([arr])

def sort(arr):
    i = 0
    while i < (len(arr)):
        j = 0
        while j < (len(arr) - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
            j += 1    
        i += 1

sort([1, 3245242, 23, 5432, 54566, 432])
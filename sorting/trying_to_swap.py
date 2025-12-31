def sw(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    print(arr)

def sort(arr):
    i = 0
    for i in range(0, len(arr), 1):
        j = 0
        for j in range(0, len(arr) - 1, 1):
            if arr[j] > arr[j + 1]:
                sw(arr, j, j + 1)
            j += 1
        i += 1
        print(arr)

sort([45, 23, 12, 1, 0.5])
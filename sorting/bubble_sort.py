arr = [3, 7, 2, 7, 2, 7, 4, 7, 1421, 0.21, 42]

def swap(arr, i, j):
    c = arr[i]
    arr[i] = arr[j]
    arr[j] = c

for i in range(0, len(arr), 1):
    for j in range(0, len(arr) - 1, 1):
        if arr[j] > arr[j + 1]:
            swap(arr, j, j + 1)
        
        j += 1
    i += 1

print(arr)
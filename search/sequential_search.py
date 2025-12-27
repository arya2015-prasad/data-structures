def search(arr, num):
    I = 0
    false_condition = -1

    while (I < len(arr)):
        I += 1
        if num == arr[I]:

            false_condition = I
            return I
            
        else:
            break
            return false_condition

arr = [43, 34623, 253, 664, 4335]
num = 664

print(search(arr, num))
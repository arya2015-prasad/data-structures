
def swap_arr_index(arr, i, j):
    f = arr[i]
    arr[i] = arr[j]
    arr[j] = f

# 4, 5, 2, 6
# 4, 5, 2, 6
# 5, 4, 2, 6
# 5, 4, 2, 6
# 5, 4, 2, 6
# 6, 4, 2, 5
# 


def index_of_bigest(arr, from_index): # 1
    
    big_index = from_index
    print("from index ", from_index)
    while from_index < len(arr):
        if arr[big_index] > arr[from_index]:
            big_index = from_index
        from_index += 1
        
    print("big index is ", big_index)    
    return big_index

def sort_asc(arr):
    i = 0
    j = 0
    while i < len(arr):
        print()
        print(arr)
        j = index_of_bigest(arr, i) # i = 1, j = 2
        swap_arr_index(arr, i, j)           
        i += 1
        print(arr)
    return arr
    

print(sort_asc([4, 5, 2, 6]))
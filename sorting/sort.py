'''
arr = []
q = int(input("Enter array length: "))
for x in range(q):
    num = float(input("Enter nums: "))
    arr.append(num)
    print(arr)
'''

def swap(arr, i, j):
    c = arr[i]
    arr[i] = arr[j]
    arr[j] = c
    print(f"array {arr}, i{i}, j{j}")

def sort(arr):
    
    i = 0
    length = len(arr)
    for i in range(0, len(arr), 1):
        
        j = 0
        
        for j in range (0, length-1, 1):
           
            if arr[j] > arr[j + 1]:
                swap(arr, j, j+1)
                
            j += 1
            
        i += 1
        
  
    

sort([10, 3, 534, 645433, 3664, 4326])

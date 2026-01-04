def ins():    
    array = [4, 3, 6, 2, 7, 2, 3, 7, 4]


    for i in range(1, len(array), 1):
        insert_index = i
        cv = array.pop(i)

        for j in range(i - 1, -1, -1):
            if array[j] > cv:
                insert_index = j
        
        array.insert(insert_index, cv)
    return array

print(ins())
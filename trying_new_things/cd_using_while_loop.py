def largest(arr):
    large = -4352543253245
    i = 0
    while i < len(arr):
        if arr[0] < arr[i]:
            arr[0] = arr[i]
        i += 1
    return large

print(largest([4, 6242, 52542345, 6244, 0.9, 0.25]))
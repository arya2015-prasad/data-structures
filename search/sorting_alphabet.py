def sw(arr, c, d):
    a = arr[c]
    arr[c] = arr[c+1]
    arr[c+1] = a
    print(f"arr{arr}, c{c}, d{d}")
    print()

def so(arr):
    d = 0
    while (d < len(arr)):
        c = 0
        while (c < len(arr) - 1):
            if ord(arr[c]) > ord(arr[c+1]):
                sw(arr, c, c+1)
            c += 1
        d += 1

so(["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"])
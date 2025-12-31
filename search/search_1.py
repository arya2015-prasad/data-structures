def s(string, tv):
    for x in range(len(string)):
        if string[x] == tv:
            return x
        
    return -1

e = "Hello world"
i = "w"

result = s(e, i)

if result != -1:
    print(f"found at index {result}")

else:
    print(f"Not found")
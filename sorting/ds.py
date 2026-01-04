dicti = {
            "A" : "65", 
            "B" : "66",
            "C" : "67",
            "D" : "68",
            "E" : "69", 
            "F" : "70",
            " " : "--"
}

def encrypting(string):
    n = len(string)
    encrypted_string = ""
    for x in range(0, n, 1):
        encrypted_string += str(dicti.get(string[x]))
        print(str(x) + " "+ encrypted_string)
    return encrypted_string

print(encrypting("ABCDEF EDC"))
h = int(input("Enter numbers: "))

mh = h
mha = h

while h != 0:
    if mh > h:
        mh = h
    
    if mha < h:
        mha = h

    h = int(input("Enter numbers: "))

print("min num is {}".format(mh, ","))
print("max num is {}".format(mha, ","))
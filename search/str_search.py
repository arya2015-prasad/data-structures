x = 0 # index for sub string
y = 0 # index for the whole string

string = input("Enter a text [can be annything!]: ")
sub = input("Enter what do U want 2 find in da text: ")

while x < len(string) and y < len(sub):
    if string[x] == sub[y]:
        y += 1
        x += 1
    else:
        y = 0
        x += 1

position = x - y
print(f"The position of {sub} is found at: {position}.")
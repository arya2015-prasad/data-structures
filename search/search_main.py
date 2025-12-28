from sequential_search import search

baseString = []

def menu():
    print("menu")
    print("")
    print("1. search in string")
    print("2. search in array")
while True:
  menu()
  print()
  x = int(input("Enter your choice: "))
  match x:
   case 2:
    how_many = "Enter array's length: "
    jk = input(how_many)
    sx = int(jk) 
    
    for x in range(sx):
     baseSt = "Enter chars: "
     
     que = input(baseSt)
     
     baseString.append(que)

    searchString = "What number do you want to find in the array: "
    qu = input(searchString)

    print(search(baseString, searchString))

while True:
    baseString = "Enter a text: "
    q = input(baseString)

    searchString = "What do you want to find in the text: "
    q = input(searchString)

    print(search(baseString, searchString))
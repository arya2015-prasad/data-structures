from an_psuedo import s
from psuedo import search
from str_search import substr
from str_search import substr
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
   case 1:
    baseString = input("Enter the string: ")
    searchString = input("Enter the substring: ")
    print(s(baseString, searchString))
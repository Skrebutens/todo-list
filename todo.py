# 
# Todo App
# 
# Masivi https://mape.gov.lv/catalog/materials/6501426F-B6EC-44B3-8B93-DC553DAE8886/view?preview=7A90D16F-0A8A-4840-A2E3-5EA4F6D4E194
# Lists https://www.w3schools.com/python/python_lists.asp
# 

def add(list, item):
  list.append(item)
  pass


def remove(list, index):
  list.pop(index)
  print(list)
  pass


def clear(list):
  list.clear()
  print(list)
  pass


def print_list(list):
  for x in list:
    print(x)
  pass


def show(list):
  print(list[1])
  pass


list = []

print("List is empty now, what you want to do?")
while True:

  choice = int(input("1. Add\n2. Remove\n3. Clear\n4. Print list\n5. Show item by index "))
  if choice == 1:
    item = input("What you want to add?\n")
    add(list, item)
    print(list)
    print("You added")

  elif choice == 2:
    index = int(input("What you want to remove?\n"))
    remove(list, index)
    print_list(list)

  elif choice == 3:
    print("You cleared your list")
    clear(list)
    print(list)

  elif choice == 4:
    print(list)

  elif choice == 5:
    show(list)
  else:
    print("Invalid input")

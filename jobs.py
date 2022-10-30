import controller as _c

c = _c.Controller()


print("Choose your option")
print("1. Get data from pracuj")
print("2. Get data from indeed")
print("3. Get data from olx")
print("4. Get data from everywhere")
print("5. Show data from pracuj")
print("6. Show data from indeed")
print("7. Show data from olx")
print("8. Show data from everywhere")
print("9. Exit")

option = input("Your option: ")
c.choose_option(option)

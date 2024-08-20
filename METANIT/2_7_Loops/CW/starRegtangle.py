'''a = int(input("Enter number of side: "))
b = int(input("Enter number of another side: "))

for i in range(a):
    print("*", end = " ")

for i in range(b):
    print("*", "  ", "*")

for i in range(a):
    print("*", end = " ")'''

a = int(input("Enter number of side: "))
b = int(input("Enter number of another side: "))

sym = "*"
symEmpty = "#"
str = ""

for row in range(a):
    for col in range(b):
        if row == 0 or row == a-1:
            str += sym
        else:
            if col == 0 or col == b-1:
                str += sym
            else:
                str += symEmpty
    str += "\n"
print(str)
print("Когда в зал?")
'''a = int(input("Enter number of side: "))
b = int(input("Enter number of another side: "))

for i in range(a):
    print("*", end = " ")

for i in range(b):
    print("*", "  ", "*")

for i in range(a):
    print("*", end = " ")'''

#a = int(input("Enter number of side: "))
a = 3
b = 5
#b = int(input("Enter number of another side: "))

sym = "*"
symEmpty = "#"
str = ""

row = 0
for i in range(a):
    for j in range(a):
        if row == 0:
            str += sym
        else:
            str += symEmpty
    print(row)
    row += 1
    str += "\n"
    print(sym)

print(str)

''' count = int(input("Enter any number I should count to: "))
for n in range(count):
    print(n, end=" ")


number = 1
 
while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")

message = str(input("Enter any word: "))

for c in message:
    print(c)

number = 1
while number < 5:
    print(f"number = {number}")
    number += 1
print("Работа программы завершена")
'''

i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1

number = 0
while number < 5:
    number += 1
    if number == 3 :    # если number = 3, выходим из цикла
        break
    print(f"number = {number}")
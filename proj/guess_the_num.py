import random
rand_num = random.randint(1, 10)
num = 0

while rand_num != num:
    num = int(input("Guess number from 1 to 10: "))
    print("Try again :/")

print("Great job!!")
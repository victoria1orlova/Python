def printMultiTable(num):
    for i in range(2, 11):
     print(f"{num} x {i} = {i * num}")

for a in range(2, 10):
   print()
   print("   ", a)
   printMultiTable(a)
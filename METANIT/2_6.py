'''
Напишиите программу, которая вычисляет сумму скидки в зависимости от суммы продажи. Пусть скидки установлены следующим образом:

Сумма продажи	Скидка
0-5000	5%
5000-15000	12%
15000-25000	20%
свыше 25000	30%
После вычисления скидки программа должна вывести саму скидку и сумму с вчетом скидки. Например:

Введите сумму продажи: 25000
Скидка:  5000.0
Сумма с учетом скидки :  20000.0
'''

a = float(input("Enter number a: "))
b = float(input("Enter number b: "))

if a > b:
    print(f"The largest number: {a}")
elif a < b:
    print(f"The largest number: {b}")
else:
    print(f"There is no largest number {a} = {b}")

# ввод года
y=int(input("Введите год: "))
 
# проверка года
if y%400==0 or y%4==0 and y%100!=0:
    print("Год високосный")
else:
    print("Год не високосный")

ppl = float(input("Enter how many people: "))
comp = float(input("Enter how many computers: "))

if ppl > comp:
    print("Then someone will use tablet")
elif ppl == comp:
    print("Lucky you!!")
else:
    print("Lucky you!!")
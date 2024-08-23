#функция которая принимает строку и на выходе строка в рамке
line = str(input("Enter something: "))
length = len(line)

def lineInFrame(line):
    sym = "*"
    framedStr = ""
    #print(line, length)

    #верхушка
    framedStr += sym * (length + 2) + "\n"

    #середина
    framedStr += sym + line + sym + "\n"

    #низ
    framedStr += sym * (length + 2) + "\n"
    print(framedStr)

lineInFrame(line)
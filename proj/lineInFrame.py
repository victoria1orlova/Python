#функция которая принимает строку и на выходе строка в рамке
line = str(input("Enter something: "))

def drawUnicodeBox(line):
    length = len(line)

    # верхняя граница
    topBorder = "\u2554" + "\u2550" * (length) + "\u2557"
    print(topBorder)

    # боковые границы 
    
    middle = "\u2551" + line + "\u2551"
    print(middle)

    # нижняя граница
    bottomBorder = "\u255a" + "\u2550" * (length) + "\u255d"
    print(bottomBorder)

drawUnicodeBox(line)


'''
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

'''
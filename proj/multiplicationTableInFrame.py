def printMultiTable(num):
    result = ""
    for i in range(2, 11):
        result += f"{num} x {i} = {i * num}\n"
    return result

def drawFrame(multiplicationTable):
    lines = multiplicationTable.strip().split('\n')
    length = max(len(line) for line in lines) + 2

    # верхняя граница
    topBorder = "\u2554" + "\u2550" * length + "\u2557"
    print(topBorder)

    # боковые границы
    for line in lines:
        print("\u2551" + line.center(length) + "\u2551")

    # нижняя граница
    bottomBorder = "\u255a" + "\u2550" * length + "\u255d"
    print(bottomBorder)

for a in range(2, 10):
    print()
    print("   ", a)
    multiplicationTable = printMultiTable(a)
    drawFrame(multiplicationTable)

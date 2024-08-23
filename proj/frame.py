def drawUnicodeBox(width, height):
    if width < 2 or height < 2:
        print("Ширина и высота должны быть не менее 2")
        return
    # верхняя граница
    topBorder = "\u2554" + "\u2550" * (width - 2) + "\u2557"
    print(topBorder)

    # боковые границы 
    for _ in range(height - 2):
        middle = "\u2551" + " " * (width - 2) + "\u255d"
        print(middle)

    # нижняя граница
    bottomBorder = "\u255a" + "\u2550" * (width - 2) + "\u255d"
    print(bottomBorder)

# запрос у пользователя ширины и высоты рамки
width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))

drawUnicodeBox(width, height)
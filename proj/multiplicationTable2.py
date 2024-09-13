def multiplicationTable():
    height = 10
    width = 10

    topBorder = "\u2554" + "\u2550" * (width * 4) + "\u2557"
    print(topBorder)

    for i in range(1, height + 1):
        row_str = "\u2551"
        for a in range(1, width + 1):
            row_str += f"{i * a:2} \u2551"
        print(row_str)

        if i < height:
            print("\u2560" + "\u2550" * (width * 4) + "\u2563")
        else:   
            print("\u255A" + "\u2550" * (width * 4) + "\u255D")

multiplicationTable()


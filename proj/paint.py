def draw_pyramid(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))

# Задаем высоту пирамиды
height = 5
draw_pyramid(height)

numbers = [10, 20, 30, 5, 25]
max_num = numbers[0]
for num in numbers:
    if num > max_num:  # Use 'max_num' instead of 'max'
        max_num = num
print(max_num)

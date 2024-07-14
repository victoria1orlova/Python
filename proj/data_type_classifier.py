user_input = input("Введите что-нибудь: ")

# bool, str, int, float, complex

if user_input.lower() in ['true', 'false']:
    print("Тип данных: bool")
try:
    int(user_input)
    print("Тип данных: int")
except ValueError:
    pass
try:
    float(user_input)
    print("Тип данных: float")
except ValueError:
    pass
try:
    str(user_input)
    print("Тип данных: str")
except ValueError:
    pass
try:
    complex(user_input)
    print("Тип данных: complex")
except ValueError:
    pass
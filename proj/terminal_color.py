from colorama import init, Fore, Style

# Инициализируем colorama
init()

# Функция для изменения цвета текста в терминале
def change_text_color(text, color):
    if color == 'red':
        print(Fore.RED + text + Style.RESET_ALL)
   

'''change_text_color('Hello, World!', 'red')
change_text_color('This is a test message.', 'green')
change_text_color('Color change example.', 'yellow')
change_text_color('Another message.', 'blue')
'''
terminal_color = input("Enter color: ")
user_input = input("Enter anything you want: ")
if terminal_color == 'red':
     print(Fore.RED + user_input + Style.RESET_ALL)
elif terminal_color == 'green':
        print(Fore.GREEN + user_input + Style.RESET_ALL)
elif terminal_color == 'yellow':
        print(Fore.YELLOW + user_input + Style.RESET_ALL)
elif terminal_color == 'blue':
        print(Fore.BLUE + user_input + Style.RESET_ALL)
else:
        print(user_input)
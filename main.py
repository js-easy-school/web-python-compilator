# Импортировать модуль sys для доступа к стандартному потоку вывода
import sys

# Определить функцию print, которая будет выводить текст в стандартный поток вывода
def print(*args, **kwargs):
    # Вывести текст в стандартный поток вывода
    sys.stdout.write(' '.join(map(str, args)) + '\n')

# Определить функцию для обработки ввода и выполнения выражений
def handle_input(input_text):
    try:
        # Выполнить введенное выражение и вывести результат
        result = eval(input_text)
        print(result)
    except Exception as e:
        # В случае ошибки вывести сообщение об ошибке
        print('Error:', e)

# Пример использования
handle_input("print('Hello, world!')")  # Выводит "Hello, world!" в стандартный поток вывода
handle_input("1 + 2")  # Выводит "3" в стандартный поток вывода

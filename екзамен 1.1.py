def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ділення на нуль неможливе"

def open_file(name):
    try:
        with open(name, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Файл не знайдено"

print(divide(10, 0))
print(open_file("test.txt"))

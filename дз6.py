try:
    user_input = input("Введіть число: ")
    number = int(user_input)
    print("Ви ввели число:", number)

except ValueError:
    print("Помилка: введені дані не можна конвертувати в ціле число.")

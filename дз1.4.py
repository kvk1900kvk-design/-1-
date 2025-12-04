score = int(input("Введіть кількість балів (0—100): "))

if score < 50:
    print("Незадовільно")
elif score < 70:
    print("Задовільно")
elif score < 90:
    print("Добре")
elif score <= 100:
    print("Відмінно")
else:
    print("Бали введено некоректно")

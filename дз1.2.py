import random

secret = random.randint(1, 10)
attempts = 3

print("Я загадав число від 1 до 10. Спробуй вгадати!")

for i in range(attempts):
    guess = int(input("Введіть число: "))

    if guess == secret:
        print("Вітаю! Ви вгадали!")
        break
    elif guess > secret:
        print("Менше")
    else:
        print("Більше")
else:
    print(f"Ви не вгадали! Було загадано число {secret}.")

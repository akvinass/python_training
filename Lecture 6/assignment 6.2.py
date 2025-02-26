user_input = int(input("Введіть число від 0 до 8639999): "))

if 0 <= user_input < 8640000:
    days = user_input // 86400
    hours = (user_input % 86400) // 3600
    minutes = (user_input % 3600) // 60
    seconds = user_input % 60

    if days % 10 == 1 and days % 100 != 11:
        day_spell = "день"
    elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
        day_spell = "дні"
    else:
        day_spell = "днів"

    print(f"{days} {day_spell}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
else:
    print("Число повинно бути від 0 до 8639999!")
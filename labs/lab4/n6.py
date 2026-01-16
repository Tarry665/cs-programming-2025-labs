try:
    year = int(input("Введите год: "))
    if year % 4 == 0 and year % 100 != 0:
        print(year, " - високосный год")
    else:
        if year % 400 == 0:
            print(year, "- високосный год")
        else:
            print(year, "- не високосный год")
except ValueError:
    print("Ошибка, введите число!")

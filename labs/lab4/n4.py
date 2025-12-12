try:
    x = int(input("введите число: "))
    if x % 3 == 0 and x % 2 == 0:
        print("Число делится на 6.")
    else:
        print("Число не делится на 6.")
except ValueError:
    print("Нужно ввести число, роблан!")

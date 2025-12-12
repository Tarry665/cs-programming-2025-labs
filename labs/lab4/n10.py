try:
    n = int(input("Введите число: "))
    if n < 0:
        print("Ошибка: число должно быть неотрицательным")
    elif n == 0:
        print("0 - не простое и не составное число")
    elif n == 1:
        print("1 - не простое и не составное число")
    else:
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} - составное число")
                break
        else:
            print(f"{n} - простое число")
except ValueError:
    print("Нужно ввести число, роблан!")
try:
    num = input("Введите три числа через пробел: ")
    a, b, c = num.split()
    if a < b and a < c:
        minimum = a
    elif b < a and b < c:
        minimum = b
    else:
        minimum = c
    print(minimum)
except ValueError:
    print("Нужно ввести 3 числа через пробел, роблан!")
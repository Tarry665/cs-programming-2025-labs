a = int(input("Введите число от 1 до 9: "))
if 0<a<10:
    for i in range(1, 11):
        print(a, "*", i, "=", a*i)
else:
    print("Вы ввели неправильно!")

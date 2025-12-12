num = input("Введите три числа: ")
a, b, c = num.split()
if a < b and a < c:
    minimum = a
elif b < a and b < c:
    minimum = b
else:
    minimum = c
print(minimum)
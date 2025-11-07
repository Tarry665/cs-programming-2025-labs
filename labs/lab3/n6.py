fib = int(input("Введите число:"))
a = 0
b = 1
print(a)
print(b)
for i in range(0,fib + 1):
    if i == a + b:
        a = b
        b = i
        print(i)
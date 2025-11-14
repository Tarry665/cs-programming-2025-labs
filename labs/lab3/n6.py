f = int(input("Введите число:"))
# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(0, f + 1):
#     if i == a + b:
#         a = b
#         b = i
#         print(i)


a = 0
b = 1

while f > (a + b):
    c = a
    a = b
    b = b + c
    print (b)
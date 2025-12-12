x = int(input("Введите сумму покупки: "))
if x < 1001 and x > 0:
    discount = 0
    print(f"Ваша скидка: {discount}%")
    print(f"к оплате: {x}")
elif x > 1000 and x < 5001:
    discount = 5
    print(f"Ваша скидка: {discount}%")
    print(f"к оплате: {x * 0.95}")
elif x > 5000 and x < 10001:
    discount = 10
    print(f"Ваша скидка: {discount}%")
    print(f"к оплате: {x * 0.9}")
elif x > 10000:
    discount = 15
    print(f"Ваша скидка: {discount}%")
    print(f"к оплате: {x * 0.85}")

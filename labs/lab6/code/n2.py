def vklad(s, years):
    if s < 30000:
        print("Error!")
        return
    
    bonus = s // 10000 * 0.3
    if bonus > 5:
        bonus = 5
    
    if years <= 3:
        base = 3
    elif years <= 6:
        base = 5
    else:
        base = 2
    
    total_rate = base + bonus
    
    money = s
    year = 0
    while year < years:
        money = money + money * total_rate / 100
        year = year + 1
    
    profit = money - s
    print(round(profit, 2))
print(vklad(70000,5))

s = int(input("Введите количество рублей: "))
years = int(input("Введите количество лет: "))
vklad(s, years)

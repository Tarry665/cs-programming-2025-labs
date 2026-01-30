a = {"bread": 20, "ice cream": 40, "toilet paper": 200, "juice": 30}
lowest = min(a, key = a.get)
highest = max(a, key = a.get)
print(f"Минимальная цена: {lowest} {a[lowest]}")
print(f"Максимальная цена: {highest} {a[highest]}")
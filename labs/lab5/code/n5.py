products = {'яблоки': 100, 'бананы': 50, 'апельсины': 150, 'молоко': 80, 'хлеб': 40}

min_p = min(products, key=products.get)
max_p = max(products, key=products.get)

print(f"Минимальная цена: {min_p} - {products[min_p]}")
print(f"Максимальная цена: {max_p} - {products[max_p]}")
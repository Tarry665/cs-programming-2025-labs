def convert_time(n, source_unit, target_unit):
    # Переводим в секунды
    if source_unit == "h":
        total_seconds = n * 3600
    elif source_unit == "m":
        total_seconds = n * 60
    elif source_unit == "s":
        total_seconds = n
    else:
        total_seconds = n
    
    if target_unit == "h":
        result = total_seconds / 3600
    elif target_unit == "m":
        result = total_seconds / 60
    elif target_unit == "s":
        result = total_seconds
    else:
        result = total_seconds
    
    print(str(result) + target_unit)

n = float(input("Введите количество: "))
source_unit = input("Введите исходную единицу (h/m/s): ")
target_unit = input("Введите целевую единицу (h/m/s): ")
convert_time(n, source_unit, target_unit)

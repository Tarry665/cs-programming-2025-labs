try:    
    x = int(input("Введите час (0-23): "))
    if x >= 0 and x < 6:
        time = "ночь"
    elif x >= 6 and x < 12:
        time = "утро"
    elif x >= 12 and x < 18:
        time = "день"
    elif x >= 18 and x < 24:
        time = "вечер"
    else:
        print("Введённое вами число не входит в промежуток 0-23.")
    print(f"Сейчас {time}")
except ValueError:
    print("Нужно ввести число, роблан!")
    


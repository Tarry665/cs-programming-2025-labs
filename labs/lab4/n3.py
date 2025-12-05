try:

    age = int(input("введите возраст собаки (в годах): "))
    if age > 0 and age < 23:
        if age == 1 or age == 2:
            dog_age = age * 10.5
        else:
            dog_age = age * 4 + 13
        print("Возраст собаки в человеческих годах: ",dog_age)
    else:
        print("вы ввели неправильно!")

except ValueError:
    print("нужно ввести число, роблан!")
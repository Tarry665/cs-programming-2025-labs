eng_rus_dict = {
    "apple": "яблоко",
    "banana": "банан",
    "dog": "собака",
    "wear": "носить",
    "knee": "колено"
}

rus_eng_dict = {value: key for key, value in eng_rus_dict.items()}

russian_word = input("Введите русское слово: ")

if russian_word in rus_eng_dict:
    print(f"Перевод: {rus_eng_dict[russian_word]}")
else:
    print("Слово не найдено в словаре")
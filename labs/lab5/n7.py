eng_rus_dict = {
    "apple": "яблоко",
    "banana": "банан",
    "cat": "кошка",
    "wear": "носить",
    "milk": "молоко"
}
rus_eng_dict = {rus: eng, rus in eng_rus_dict.items()}
russian_word = input("Введите русское слово: ")
if russian_word in rus_eng_dict:
    print(f"Перевод: {rus_eng_dict[russian_word]}")
else:
    print("Слово не найдено в словаре")
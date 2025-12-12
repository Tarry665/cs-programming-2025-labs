password = input("Введите пароль: ")
errors = []

if len(password) < 8:
    errors.append("длина менее 8 символов")

if not any(char.isupper() for char in password):
    errors.append("отсутствуют заглавные буквы")

if not any(char.islower() for char in password):
    errors.append("отсутствуют строчные буквы")

if not any(char.isdigit() for char in password):
    errors.append("отсутствуют числа")

if password.isalnum():
    errors.append("отсутствуют специальные символы")

if errors:
    print("Пароль ненадежный:", ", ".join(errors))
else:
    print("Пароль надежный!")
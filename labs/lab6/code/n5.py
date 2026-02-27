def check_palindrome():
    s = input().strip()
    cleaned = ""
    
    for c in s:
        if c.isalnum():
            cleaned += c.lower()
    
    reversed_cleaned = cleaned[::-1]
    
    if cleaned == reversed_cleaned:
        print("Да")
    else:
        print("Нет")

check_palindrome()
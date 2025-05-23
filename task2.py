####Необхідно розробити функцію, яка приймає рядок як вхідний параметр,
# додає всі його символи до двосторонньої черги (deque з модуля collections в Python),
# а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом.
# Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів,
# а також бути нечутливою до регістру та пробілів.
from collections import deque


def is_palindrome(text: str) -> bool:
    d = deque()
    for char in text:
        if char.isalnum():
            d.append(char.lower())

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


print(is_palindrome('вимив'))
print(is_palindrome('Алла'))
print(is_palindrome('hello world'))
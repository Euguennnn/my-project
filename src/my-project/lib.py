"""
lib.py

Модуль з допоміжними функціями для лабораторної роботи №1
з курсу "Програмування скриптовими мовами" (DevOps basics).

Демонструє механізм оформлення повторно використовуваного коду
у вигляді окремого модуля, який імпортується в main.py.
"""


def factorial(n: int) -> int:
    """
    Обчислює факторіал невід'ємного цілого числа n (n!).

    :param n: невід'ємне ціле число
    :return: значення n!
    """
    if n < 0:
        raise ValueError("Факторіал визначений лише для невід'ємних чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_palindrome(text: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом (без урахування регістру
    та пробілів).

    :param text: вхідний рядок
    :return: True, якщо рядок є паліндромом, інакше False
    """
    normalized = text.lower().replace(" ", "")
    return normalized == normalized[::-1]


def count_vowels(text: str) -> int:
    """
    Підраховує кількість голосних літер (латиниця) у рядку.

    :param text: вхідний рядок
    :return: кількість голосних літер
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in text if ch in vowels)


def fibonacci(n: int) -> list:
    """
    Генерує перші n чисел послідовності Фібоначчі.

    :param n: кількість чисел, які потрібно згенерувати
    :return: список перших n чисел Фібоначчі
    """
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

"""
test.py

Прості перевірки (тести) для функцій модуля lib.py.
Файл додається у feature-гілці (feature/add-tests) для демонстрації
роботи з Git у цій лабораторній роботі.
"""

from lib import factorial, is_palindrome, count_vowels, fibonacci


def test_factorial():
    """Перевіряє коректність обчислення факторіалу."""
    assert factorial(0) == 1
    assert factorial(5) == 120


def test_is_palindrome():
    """Перевіряє розпізнавання паліндромів."""
    assert is_palindrome("потоп") is True
    assert is_palindrome("python") is False


def test_count_vowels():
    """Перевіряє підрахунок голосних літер."""
    assert count_vowels("DevOps") == 2


def test_fibonacci():
    """Перевіряє генерацію послідовності Фібоначчі."""
    assert fibonacci(5) == [0, 1, 1, 2, 3]


if __name__ == "__main__":
    test_factorial()
    test_is_palindrome()
    test_count_vowels()
    test_fibonacci()
    print("Усі тести пройдено успішно!")

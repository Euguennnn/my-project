"""
main.py

Точка входу програми. Імпортує функції з модуля lib
та демонструє їх роботу.
"""

from lib import factorial, is_palindrome, count_vowels, fibonacci


def main():
    """Головна функція програми: викликає функції з lib та виводить результати."""

    # 1. Обчислення факторіалу
    number = 6
    print(f"Факторіал числа {number} = {factorial(number)}")

    # 2. Перевірка рядка на паліндром
    word = "А роза упала на лапу Азора"
    result = is_palindrome(word)
    print(f'Рядок "{word}" є паліндромом: {result}')

    # 3. Підрахунок голосних літер
    sentence = "DevOps and Python scripting lab"
    vowels_count = count_vowels(sentence)
    print(f'Кількість голосних (латиниця) у реченні "{sentence}": {vowels_count}')

    # 4. Генерація послідовності Фібоначчі
    n_terms = 10
    fib_sequence = fibonacci(n_terms)
    print(f"Перші {n_terms} чисел Фібоначчі: {fib_sequence}")


if __name__ == "__main__":
    main()

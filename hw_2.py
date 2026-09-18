import re
from typing import Callable


def generator_numbers(text: str):
    """
    Ітерує по всіх числах float відокремлених пробілами.
    :param text: рядок, в якому функція шукає числа
    :return: кожне число float
    """
    numbers = re.findall(r'\d+\.\d+', text)
    for number in numbers:
        yield float(number)


def sum_profit(text: str, func: Callable):
    """
    Обчислює загальну суму чисел у вхідному рядку.
    :param text: рядок, з якого функція бере числа для обчислення
    :param func: функція для отримання чисел float з рядка
    :return: суму чисел
    """
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f'Загальний дохід: {total_income}')  # Загальний дохід: 1351.46

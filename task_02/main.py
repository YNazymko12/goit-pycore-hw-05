from decimal import Decimal
import re
from typing import Callable

def generator_numbers(text: str):
    # Використовуємо регулярний вираз для знаходження всіх дійсних чисел у тексті
    pattern = r"\b\d+\.\d+\b"
    matches = re.findall(pattern, text)

    # Створення генератора для повернення чисел по одному
    for match in matches:
        yield Decimal(match)

def sum_profit(text: str, func: Callable):
    # Виклик генератора, щоб отримати всі числа з тексту
    numbers_generator = func(text)

    # Обчислення загальної суми чисел
    total = sum(numbers_generator)
    return total


# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
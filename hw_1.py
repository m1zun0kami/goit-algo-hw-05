def caching_fibonacci():
    """
    Створює та використовує кеш для зберігання і повторного використання вже обчислених значень чисел Фібоначчі.
    :return: внутрішню функцію fibonacci(n)
    """
    cache = {}

    def fibonacci(n):
        """
        Обчислює число фибоначі за номером n.
        :param n: номер числа в рядку Фібоначчі
        :return: число n; якщо число вже кешоване - значення з кешу
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:    # перевірка можливості повернути значення з кешу, щоб не обчислювати повторно
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci


fib = caching_fibonacci()
print(fib(10))  # 55
print(fib(15))  # 610
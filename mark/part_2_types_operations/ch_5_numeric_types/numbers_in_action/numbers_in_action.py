def program_1() -> None:
    a = 10.0
    с = 10
    b = 2
    # любое деление в Python возвращает вещественное число
    print(type(a / b), a / b)
    print(type(с / b), с / b)
    # Целочисленное деление
    # Возвращает целочисленное значение, если оба числа целые
    # Если одно из чисел не целое, то возвращается вещественное
    print(type(a // b), a // b)
    print(type(с // b), с // b)
    pass


program_1()
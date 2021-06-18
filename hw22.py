"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def even_odd(number, even = 0, odd = 0):
    if number == 0:
        print("Четных - {0}/Нечетных - {1}".format(even, odd))
    else:
        numeral = number % 10
        number = number // 10
        if numeral % 2 == 0:
            even += 1
        else:
            odd += 1
        return even_odd(number, even, odd)

even_odd(34560)
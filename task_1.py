"""
Я бы воспользовался numpy, но не знаю, приветствуется это проверяющим или нет,
поэтому все сделано без сторонних библиотек.
P.S. Python 3.8
"""
from math import sqrt


def get_unique_elements(data: list):
    unique_elements = []
    for e in data:
        if e not in unique_elements:
            unique_elements.append(e)
    return unique_elements


def str_sorted_info(data: list):
    count = {}
    for e in data:
        if e in count:
            count[e] += 1
        else:
            count[e] = 1
    list_d = list(count.items())
    list_d.sort(reverse=True)
    list_d.sort(key=lambda i: i[1], reverse=True)
    string = ""
    for e in list_d:
        string += f"({e[0]}: {e[1]}), "
    return string


if __name__ == '__main__':
    DATA = [13, 29, 37, 49, 29, 7, 25, 5, 50, 2, 18, 0, 14, 16, 14, 4, 6, 14, 2, 5, 41, 27, 10, 11, 33, 6, 7, 47,
            35, 35, 48, 0, 38, 1, 41, 15, 26, 46, 4, 23, 5, 32, 45, 37, 2, 33, 20, 30, 46, 20, 10, 14, 44, 25, 3,
            27, 6, 22, 9, 20, 18, 43, 5, 33, 27, 41, 38, 20, 6, 2, 18, 29, 34, 40, 41, 8, 44, 30, 21, 10, 6, 1, 12,
            0, 22, 28, 47, 4, 5, 1, 11, 21, 1, 44, 24, 42, 42, 41, 14, 24]
    print(f"1. Уникальные элементы: {get_unique_elements(DATA)}")
    print(f"2. Список чисел <= 40, не встречающихся в исходном списке: {[i for i in range(0, 41) if i not in DATA]}")
    print(f"3. {str_sorted_info(DATA)}")
    print(f"4. Среднеквадратичное отклонение: {sqrt(sum((x-sum(DATA)/len(DATA))**2 for x in DATA)/(len(DATA)))}")

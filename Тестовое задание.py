import math


def find_unique(value: list) -> list:
    """ Функция, которая принимает на вход список целых чисел и возвращает новый список,
    содержащий только уникальные элементы из исходного списка"""
    new_list = []
    for i in value:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list


def simple_num(one: int, two: int) -> list:
    """Функцию, которая принимает на вход два целых числа (минимум и максимум)
    и возвращает список всех простых чисел в заданном диапазоне"""
    primes_list = []
    for num in range(one, two):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes_list.append(num)
    return primes_list


def sorted_len_word(list_string: list) -> str:
    """Программа, которая сортирует список строк по длине,
    сначала по возрастанию, а затем по убыванию"""
    first = sorted(list_string, key=len)
    second = sorted(list_string, key=len, reverse=True)
    return f"По возрастанию {first}\nПо убыванию {second}"


class Point:
    """Класс Point, который представляет собой точку в двумерном пространстве.
    Класс должен иметь методы для инициализации координат точки, вычисления расстояния до другой точки, а также
    для получения и изменения координат."""

    def __init__(self, x_1=0, y_1=0, x_2=0, y_2=0):  # Инициализация координат
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2

    def calculate_distance(self):
        """Вычисление расстояние координат"""
        return math.sqrt((self.x_2 - self.x_1) ** 2 + (self.y_2 - self.y_1) ** 2)

    def get_coord(self):
        """Получение координат"""
        coord_x1_y1 = f"Координаты (X_1-{self.x_1}) (Y_1-{self.y_1})"
        coord_x2_y2 = f"Координаты (X_2-{self.x_2}) (Y_2-{self.y_2})"
        return coord_x1_y1, coord_x2_y2

    def set_coord(self, x_1, y_1, x_2, y_2):
        """Установка координат"""
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2



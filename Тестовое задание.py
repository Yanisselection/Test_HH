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

print(sorted_len_word(["apple", "banana", "kiwi", "orange", "grape"]))
import random

def fill_the_numbers_list(quantity):
    return [random.randint(0, 2) for _ in range(quantity)]


def delete_all_nulls(source_list):
    result_list = [number for number in source_list]

    while result_list.count(0):
        result_list.remove(0)

    return result_list


numbers_quantity = int(input('Введите количество чисел в списке: '))
numbers_list = fill_the_numbers_list(numbers_quantity)
print('Список до сжатия:', numbers_list)
print('Список после сжатия:', delete_all_nulls(numbers_list))

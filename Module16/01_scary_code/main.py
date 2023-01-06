def extend_list(source_list, additional_list):
    source_list.extend(additional_list)


def count_digit(initial_list, number):
    return initial_list.count(number)


def delete_digit(source_list, digit):
    for _ in range(source_list.count(digit)):
        source_list.remove(digit)


prime_list = [1, 5, 3]
side_list_1 = [1, 5, 1, 5]
side_list_2 = [1, 3, 1, 5, 3, 3]

extend_list(prime_list, side_list_1)
print(f'Количество цифр 5 при первом объединении: {count_digit(prime_list, 5)}')
delete_digit(prime_list, 5)

extend_list(prime_list, side_list_2)
print(f'Количество цифр 3 при втором объединении: {count_digit(prime_list, 3)}')

print('Итоговый список:', prime_list)

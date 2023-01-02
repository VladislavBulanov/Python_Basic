# Возможно, здесь решать через функцию излишне,
# просто захотелось попрактиковаться :)
def add_count_delete(source_list, additional_list, digit, merge_number, is_delete):
    source_list.extend(additional_list)
    count_digit = source_list.count(digit)
    print(f'Количество цифр {digit} при {merge_number}-ом объединении: {count_digit}')

    if is_delete:
        for _ in range(count_digit):
            source_list.remove(digit)


prime_list = [1, 5, 3]
side_list_1 = [1, 5, 1, 5]
side_list_2 = [1, 3, 1, 5, 3, 3]

add_count_delete(prime_list, side_list_1, 5, 1, True)
add_count_delete(prime_list, side_list_2, 3, 2, False)

print('Итоговый список:', prime_list)

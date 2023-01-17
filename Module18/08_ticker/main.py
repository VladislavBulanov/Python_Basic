def is_true(string_1, string_2):
    shift = abs(string_2.index(string_1[0]))

    if string_2[shift:] + string_2[:shift] == string_1:
        return shift
    else:
        return False


first_string = input('Введите первую строку: ').lower()
second_string = input('Введите вторую строку: ').lower()
result = is_true(first_string, second_string)

if result:
    print(f'Первая строка получается из второй со сдвигом {result}.')
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

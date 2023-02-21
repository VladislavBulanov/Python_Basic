import os

def run_text_calculator(data_file_path):
    total_sum = 0
    try:
        with open(data_file_path, 'r') as data_file:
            for line in data_file:
                current_line = line.strip().split()

                try:
                    validate_data(current_line)
                    total_sum += calculate_expression(current_line[0],
                                                      current_line[1],
                                                      current_line[2])
                except (SyntaxError, ValueError, ZeroDivisionError) as error:
                    print(error)

    except FileNotFoundError:
        print('Неверно указан путь к исходному файлу.')
    finally:
        print('\nСумма результатов:', total_sum)


def validate_data(data_list):
    if len(data_list) != 3:
        raise SyntaxError('Не соблюдена схема "ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2".')
    if (not data_list[0].isdigit()) or (not data_list[2].isdigit()):
        raise ValueError('Операнд не является целым числом.')


def calculate_expression(number_1, operation, number_2):
    if operation == '+':
        return int(number_1) + int(number_2)
    elif operation == '-':
        return int(number_1) - int(number_2)
    elif operation == '*':
        return int(number_1) * int(number_2)
    elif operation == '/':
        return int(number_1) / int(number_2)
    elif operation == '//':
        return int(number_1) // int(number_2)
    elif operation == '%':
        return int(number_1) % int(number_2)
    elif operation == '**':
        return int(number_1) ** int(number_2)
    else:
        raise ValueError(f'Некорректная операция: {operation}.')
# TODO Убрать эту ошибку в функцию валидности

path_to_data_file = os.path.abspath('calc.txt')
run_text_calculator(path_to_data_file)

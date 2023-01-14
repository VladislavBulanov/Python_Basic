def make_sticks_row(quantity):
    return ['I' for _ in range(quantity)]


def shot_result(current_row):
    result_row = current_row[:]
    while True:
        start_index = int(input('Сбиты палки с номера ')) - 1
        finish_index = int(input('по номер ')) - 1

        if start_index > finish_index:
            print('Неверный ввод. Номер первой палки должен быть меньше номера последней.')
        else:
            break

    result_row[start_index:finish_index + 1] = ['.' for _ in range(finish_index - start_index + 1)]
    return result_row


total_sticks = int(input('Введите количество палок: '))
total_shots = int(input('Введите количество бросков: '))

sticks_row = make_sticks_row(total_sticks)

for time in range(total_shots):
    print(f'\nБросок {time + 1}.', end=' ')
    sticks_row = shot_result(sticks_row)

print('\nРезультат:', "".join(sticks_row))

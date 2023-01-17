def digit_count(string):
    count = 0

    for symbol in string:
        if symbol.isdigit():
            count += 1

    return count


def is_upper(string):
    flag = False

    for symbol in string:
        if symbol.isupper():
            flag = True
            break

    return flag


while True:
    password = input('Придумайте пароль: ')

    if len(password) < 8:
        print('Пароль ненадёжный. Попробуйте ещё раз.\n')
    elif digit_count(password) < 3:
        print('Пароль ненадёжный. Попробуйте ещё раз.\n')
    elif not is_upper(password):
        print('Пароль ненадёжный. Попробуйте ещё раз.\n')
    else:
        print('Это надёжный пароль!')
        break

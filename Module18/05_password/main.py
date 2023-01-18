def count_digits(source_string):
    count = 0

    for symbol in source_string:
        if symbol.isdigit():
            count += 1

    return count


while True:
    password = input('Придумайте пароль: ')
    error_message = 'Пароль ненадёжный. Попробуйте ещё раз.\n'

    if len(password) < 8:
        print(error_message)
    elif password.islower():
        print(error_message)
    elif count_digits(password) < 3:
        print(error_message)
    else:
        print('Это надёжный пароль!')
        break

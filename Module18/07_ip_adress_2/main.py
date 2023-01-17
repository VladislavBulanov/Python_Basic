#TODO
def not_digit(ip_address):
    flag = False

    for element in ip_address:
        if not element.isdigit():
            return element

    return flag


def not_in_interval(ip_address):
    flag = False

    for element in ip_address:
        if int(element) > 255:
            return element

    return flag


while True:
    address = input('Введите IP-адрес: ').split('.')
    # is_not_digit = not_digit(address)
    # in_interval = not_in_interval(address)

    if not_digit(address):
        print(f'{not_digit(address)} - это не целое число.\n')
    elif not_in_interval(address):
        print(f'{not_in_interval(address)} превышает 255.\n')
    elif len(address) != 4:
        print('IP-адрес - это четыре числа, разделённые точками.\n')
    else:
        print('IP-адрес корректен.')
        break

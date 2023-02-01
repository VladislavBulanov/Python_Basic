def is_prime(source_number):
    if source_number == 0 or source_number == 1:
        return False
    elif source_number == 2 or source_number == 3:
        return True
    else:
        for current_number in range(2, source_number // 2 + 1):
            if source_number % current_number == 0:
                return False
        else:
            return True


def crypto(source_object):
    return [element for index, element in enumerate(source_object)
            if is_prime(index)]


# Tests:
# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(crypto('О Дивный Новый мир!'))
# print(crypto((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
# print(crypto({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))
# print(crypto({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

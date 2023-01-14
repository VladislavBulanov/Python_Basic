def encrypt_the_message(message, offset):
    """
    Генерируем результирующий список с помощью LC.
    Перебираем исходный текст посимвольно, получаем индекс текущей
    буквы в русском алфавите, изменяем на значение сдвига и получаем
    букву для шифра (учитываем, что можем выйти за пределы 33-х
    букв, а также, что текущий символ - пробел).

    :param message: source message for encrypt
    :type message: str
    :param offset: the value of shift
    :type offset: int
    :returns: encrypted message
    :rtype: List[str]
    """

    russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result_message = [russian_alphabet[(russian_alphabet.index(symbol) + offset) % 33]
                      if symbol != ' ' else ' '
                      for symbol in message]
    return result_message


input_message = input('Введите сообщение: ').lower()
shift = int(input('Введите сдвиг: '))

encrypted_message = encrypt_the_message(input_message, shift)
print('Зашифрованное сообщение:', "".join(encrypted_message))

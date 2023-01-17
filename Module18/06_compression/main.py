def compress(source_string):
    encrypted = []
    letter = source_string[0]
    count = 1

    for index in range(1, len(source_string)):
        if source_string[index] == letter:
            count += 1
        else:
            encrypted.append(letter)
            encrypted.append(str(count))
            letter = source_string[index]
            count = 1

    encrypted.append(letter)
    encrypted.append(str(count))
    return encrypted


string = input('Введите строку: ')
compressed = compress(string)
print('\nЗакодированная строка:', ''.join(compressed))

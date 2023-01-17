def find_longest_element(source_list):
    result = source_list[0]

    for element in source_list:
        if len(element) > len(result):
            result = element

    return result


source_text = input('Введите строку: ').split()
longest_word = find_longest_element(source_text)
print('Самое длинное слово:', longest_word)
print('Длина этого слова:', len(longest_word))

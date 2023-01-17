# TODO
input_message = input('Введите сообщение: ')
current_word = ''
result_list = []

for symbol in input_message:
    if symbol.isalpha():
        current_word = symbol + current_word
    else:
        result_list.append(current_word)
        current_word = ''
        result_list.append(symbol)

print('Новое сообщение:', "".join(result_list))

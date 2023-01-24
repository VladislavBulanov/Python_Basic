import random

limit_number = int(input('Введите максимальное число: '))
guess_number = random.randint(1, limit_number)
right_numbers = set()
wrong_numbers = set()

while (guess_numbers := input('Нужное число есть среди этих чисел: ')) != 'Помогите!':
    numbers = {int(number) for number in guess_numbers.split()}

    for current_number in numbers:
        if current_number == guess_number:
            print('Ответ Артёма: Да')
            right_numbers.update(numbers - wrong_numbers)
            break
    else:
        print('Ответ Артёма: Нет')
        right_numbers.difference_update(numbers)
        wrong_numbers.update(numbers)

print('Артём мог загадать следующие числа:', right_numbers)

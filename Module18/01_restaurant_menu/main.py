def generate_dishes_list():
    return input('Доступное меню: ').lower().split(';')


menu = generate_dishes_list()
print('\nНа данный момент в меню есть:', ", ".join(menu))

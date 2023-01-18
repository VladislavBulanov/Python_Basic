def generate_dishes_list():
    return [dish for dish in input('Доступное меню ресторана: ').lower().split(';')]


menu = generate_dishes_list()
print('\nНа данный момент в меню есть:', ", ".join(menu))

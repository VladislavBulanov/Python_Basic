from random import randint

class Warrior:
    health = 100

    def loose_health(self, damage):
        self.health -= damage


def start_fight(unit_1, unit_2):
    print('ДРАКА НАЧАЛАСЬ!')
    while unit_1.health > 0 and unit_2.health > 0:
        who_beats = randint(1, 2)
        print(f'\nБьёт воин №{who_beats}:')

        if who_beats == 1:
            unit_2.loose_health(20)
            print(f'У воина №2 осталось {unit_2.health} очков здоровья.')
        elif who_beats == 2:
            unit_1.loose_health(20)
            print(f'У воина №1 осталось {unit_1.health} очков здоровья.')

    if unit_1.health <= 0:
        print('\nПОБЕДУ ОДЕРЖАЛ ВОИН №2!')
    elif unit_2.health <= 0:
        print('\nПОБЕДУ ОДЕРЖАЛ ВОИН №1!')


warrior_1 = Warrior()
warrior_2 = Warrior()
start_fight(warrior_1, warrior_2)

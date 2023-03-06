from life import (Human, House)
from random import randint

def do_action(character):
    action_points = randint(1, 6)
    if character.satiety < 20:
        character.eat(action_points)
    elif character.house.money < 10:
        character.go_to_store(action_points)


def start_life(man_1, man_2):
    for day in range(1, 366):
        print('\nДЕНЬ {}\n'.format(day))
        do_action(man_1)
        do_action(man_2)


house = House()
human_1 = Human('Иван', house)
human_2 = Human('Андрей', house)
start_life(human_1, human_2)

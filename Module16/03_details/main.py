shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

item = input('Введите название детали: ').lower()
total_item_count = 0
total_price = 0

for element in shop:
    item_count = element.count(item)
    if item_count:
        total_price += element[1]
        total_item_count += item_count

if total_item_count:
    print('Количество деталей:', total_item_count)
    print('Общая стоимость:', total_price)
else:
    print('Такой детали в магазине нет.')

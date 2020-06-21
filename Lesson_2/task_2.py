import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as file_out:
        data = json.load(file_out)
    with open('orders.json', 'w', encoding='utf-8') as file_in:
        list_of_orders = data['orders']
        order_structure = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        list_of_orders.append(order_structure)
        json.dump(data, file_in, indent=4, ensure_ascii=False)


write_order_to_json('Обезьяна', '10', '25000', 'Central NY Zoo', '01.11.2019')
write_order_to_json('Lion', '2', '350000', 'Цирк им. Никулина', '03.06.2018')
write_order_to_json('Дельфин', '5', '75000', 'ТЦ Океания', '06.01.2020')

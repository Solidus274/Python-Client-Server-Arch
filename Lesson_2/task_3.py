import yaml

data_in = {
    'items': ['Плита', 'СВЧ-печь', 'Холодильник', 'Тостер', 'Кофеварка', 'Чайник', ],
    'items_quantity': 6,
    'items_price': {
        'Плита': '250€',
        'СВЧ-печь': '470€',
        'Холодильник': '890€',
        'Тостер': '50€',
        'Кофеварка': '100€',
        'Чайник': '25€',
    }
}

with open('file.yaml', 'w', encoding='utf-8') as file_in:
    yaml.dump(data_in, file_in, default_flow_style=False, allow_unicode=True)

with open('file.yaml', 'r', encoding='utf-8') as file_out:
    data_out = yaml.load(file_out, Loader=yaml.SafeLoader)

print(data_in == data_out)

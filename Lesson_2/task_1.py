import csv
import re

parameter_list = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']


def get_data(data):
    main_data = data.copy()
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for a in range(1, 4):
        with open('info_' + str(a) + '.txt') as file:
            i = 0
            for row in file:
                for parameter in main_data:
                    result = re.findall(rf'{parameter}', row)
                    if result == [parameter]:
                        answer = re.findall(r'\s{2,}.*$', row)
                        if i == 0:
                            os_name_list.append(answer[0].strip())
                        elif i == 1:
                            os_code_list.append(answer[0].strip())
                        elif i == 2:
                            os_prod_list.append(answer[0].strip())
                        else:
                            os_type_list.append(answer[0].strip())
                        i += 1
    return main_data, os_prod_list, os_name_list, os_code_list, os_type_list


def write_to_csv():
    dataset = list(get_data(parameter_list))
    parameters = dataset.pop(0)
    re_dataset = list(map(list, zip(*dataset)))
    print(parameters)
    with open('task_1.csv', 'w') as file:
        file_writer = csv.writer(file, delimiter=',')
        file_writer.writerow(parameters)
        for line in re_dataset:
            file_writer.writerow(line)

write_to_csv()

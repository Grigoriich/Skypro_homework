import re
from collections import Counter

from src.utils import load_json_from_path


def filter_by_string(operations_list: list, pattern: str) -> list:
    """Функция, фильтрующая список словарей транзакций по заданному описанию"""
    filtered_list = []
    for operation in operations_list:
        if "description" not in operation and pattern == "":
            return operations_list
        elif "description" in operation and re.search(pattern.lower(), operation["description"].lower()):
            filtered_list.append(operation)
    return filtered_list


def counter_by_category_list(operations_list: list, category_list: list) -> dict:
    """Функция, возвращающая словарь, где ключи - заданные категории операций,
    значения - количество операций категории в списке операций"""
    descriptions_list = []
    for operation in operations_list:
        if "description" not in operation and category_list == []:
            return operations_list
        elif "description" in operation and operation["description"] in category_list:
            descriptions_list.append(operation["description"])

        counter_category_dict = dict(Counter(descriptions_list))
    return counter_category_dict


# oper_list = load_json_from_path("../data/operations.json")
#
# descr_l = []
# for oper in oper_list:
#     if "description" in oper:
#         descr_l.append(oper["description"])
# print(Counter(descr_l))
# print([val for val in Counter(descr_l).keys()])
#
# print(len(oper_list))
# # result = filter_by_string(oper_list, "")
# result = filter_by_category_list(oper_list, ['Перевод организации', 'Открытие вклада', 'Перевод со счета на счет', 'Перевод с карты на карту', 'Перевод с карты на счет'])
# print(len(result))
# print(result)

# print(len(result))
# for oper in result:
#     if "description" in oper:
#         print(oper["description"])
#     else:
#         print(oper)
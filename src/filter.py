import re
from collections import Counter
from typing import Dict, List


def filter_by_string(operations_list: List[Dict], pattern: str) -> List[Dict]:
    """Функция, фильтрующая список словарей транзакций по заданному описанию"""
    filtered_list = []
    if pattern == "":
        return operations_list
    for operation in operations_list:
        if "description" not in operation:
            continue
        elif "description" in operation and re.search(pattern.lower(), operation["description"].lower()):
            filtered_list.append(operation)
    return filtered_list


def counter_by_category_list(operations_list: List[Dict], category_list: List) -> Dict:
    """Функция, возвращающая словарь, где ключи - заданные категории операций,
    значения - количество операций категории в списке транзакций"""
    descriptions_list = []
    if category_list == []:
        return {}
    for operation in operations_list:
        if "description" not in operation:
            continue
        elif "description" in operation and operation["description"] in category_list:
            descriptions_list.append(operation["description"])

    counter_category_dict = dict(Counter(descriptions_list))
    return counter_category_dict

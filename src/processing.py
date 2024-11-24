from multiprocessing.managers import Value
from typing import Dict, List

from src.widget import get_date_format


def filter_by_state(dictionary_list: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция, фильтрующая список словарей по ключу state"""
    if not isinstance(dictionary_list, list):
        raise TypeError("Неверный тип данных")
    result_list = []
    for item in dictionary_list:
        if not isinstance(item, dict):
            raise TypeError("Неверный тип данных")
        if "state" not in item:
            raise ValueError("Значение для фильтрации  отсутствует в исходных данных")
        if item["state"] == state:
            result_list.append(item)

    return result_list


def sort_by_date(dictionary_list: List[Dict], increase: bool = True) -> List[Dict]:
    """Функция, сортирующая список словарей по дате, с возможностью изменения порядка сортировки"""
    result_list = sorted(dictionary_list, reverse=not increase, key=lambda x: get_date_format(x["date"]))
    return result_list

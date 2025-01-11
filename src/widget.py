import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция, возвращающая замаскированный номер карты или счета с типом номера"""

    if not isinstance(number, str):
        raise TypeError("Неверный тип данных номера счёта")

    input_list = number.split()
    if len(number) == 0:
        raise ValueError("Неверный формат номера счёта")
    if len(input_list) < 2 or len(input_list[-1]) not in [16, 20]:
        raise ValueError("Неверный формат номера счёта")
    if " ".join(input_list[0:-1]).lower() not in (
        "visa classic",
        "visa platinum",
        "visa gold",
        "visa",
        "счет",
        "счёт",
        "mastercard",
        "maestro",
        "american express",
        "discover",
        "мир",
    ):
        raise ValueError("Неверный формат номера счёта")

    mask_number = ""
    if len(input_list[-1]) == 16:
        mask_number = get_mask_card_number(input_list[-1])
        input_list[-1] = mask_number
    else:
        mask_number = get_mask_account(input_list[-1])
        input_list[-1] = mask_number
    return " ".join(input_list)


def get_date(date_str: str) -> str:
    """Функция, возвращающая дату в формате ДД.ММ.ГГГГ из формата 2019-07-03T18:35:29.512364"""
    if not isinstance(date_str, str):
        raise TypeError("Неверный тип данных. Необходим строковый")

    date = date_str.split("-")
    if len(date) != 3:
        raise ValueError("Неверный формат даты")
    for date_item in date[:2]:
        if not date_item.isdigit():
            raise ValueError("Неверный формат даты")
    if not date[-1][:2].isdigit():
        raise ValueError("Неверный формат даты")
    if len(date[0]) != 4:
        raise ValueError("Неверный формат даты")
    if len(date[1]) != 2:
        raise ValueError("Неверный формат даты")
    if len(date[-1]) < 2:
        raise ValueError("Неверный формат даты")

    return f"{date[-1][:2]}.{date[1]}.{date[0]}"


def get_date_format(date_str: str) -> datetime.datetime:
    """Функция, возвращающая дату в формате даты модуля datetime из формата 2019-07-03T18:35:29.512364"""
    if not isinstance(date_str, str):
        raise TypeError("Неверный тип данных. Необходим строковый")

    date = date_str.split("-")
    if len(date) != 3:
        raise ValueError("Неверный формат даты")
    for date_item in date[:2]:
        if not date_item.isdigit():
            raise ValueError("Неверный формат даты")
    if not date[-1][:2].isdigit():
        raise ValueError("Неверный формат даты")
    if len(date[0]) != 4:
        raise ValueError("Неверный формат даты")
    if len(date[1]) != 2:
        raise ValueError("Неверный формат даты")
    if len(date[-1]) < 2:
        raise ValueError("Неверный формат даты")

    return datetime.datetime(int(date[0]), int(date[1]), int(date[-1][:2]))

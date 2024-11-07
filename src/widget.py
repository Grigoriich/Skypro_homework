from src import masks
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(number: str) -> str:
    """Функция, возвращающая замаскированный номер карты или счета с типом номера"""
    mask_number = ""
    input_list = number.split()
    if len(input_list[-1]) == 16:
        mask_number = get_mask_card_number(input_list[-1])
        input_list[-1] = mask_number
    else:
        mask_number = get_mask_account(input_list[-1])
        input_list[-1] = mask_number
    return " ".join(input_list)


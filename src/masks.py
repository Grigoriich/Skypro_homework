def get_mask_card_number(card_number: str) -> str:
    """Функция, возвращающая замаскированный номер банковской карты"""
    if len(card_number) != 16:
        raise ValueError("Неверный формат номера карты")
    if not isinstance(card_number, str):
        raise TypeError("Неверный тип данных номера карты")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, возвращающая замаскированный номер счёта"""
    return f"**{account_number[-4:]}"

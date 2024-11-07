def get_mask_card_number(card_number: str) -> str:
    """Функция, возвращающая замаскированный номер банковской карты"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, возвращающая замаскированный номер счёта"""
    return f"**{account_number[-4:]}"

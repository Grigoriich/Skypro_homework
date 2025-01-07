import logging

masks_logger = logging.getLogger(__name__)
masks_file_handler = logging.FileHandler("../logs/masks.log", mode="w")
masks_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
masks_file_handler.setFormatter(masks_formatter)
masks_logger.addHandler(masks_file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция, возвращающая замаскированный номер банковской карты"""
    masks_logger.info(f"Попытка замаскировать номер банковской карты: {card_number}")
    if not isinstance(card_number, str):
        masks_logger.error("Произошла ошибка TypeError: Неверный тип данных номера карты")
        raise TypeError("Неверный тип данных номера карты")
    if len(card_number) != 16:
        masks_logger.error("Произошла ошибка ValueError: Неверный формат номера карты")
        raise ValueError("Неверный формат номера карты")
    masks_logger.info("Номер карты успешно замаскирован")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, возвращающая замаскированный номер счёта"""
    masks_logger.info(f"Попытка замаскировать номер счёта: {account_number}")
    if not isinstance(account_number, str):
        masks_logger.error("Произошла ошибка TypeError: Неверный тип данных номера счёта")
        raise TypeError("Неверный тип данных номера счёта")
    if len(account_number) != 20:
        masks_logger.error("Произошла ошибка ValueError: Неверный формат номера счёта")
        raise ValueError("Неверный формат номера счёта")
    masks_logger.info("Номер счёта успешно замаскирован")
    return f"**{account_number[-4:]}"

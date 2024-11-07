from src import masks

CARD_NUMBER_CONST = 7000792289606361
ACCOUNT_NUMBER_CONST = 73654108430135874305

print(f"Маскировка номера карты {CARD_NUMBER_CONST}, результат: {masks.get_mask_card_number(CARD_NUMBER_CONST)}")
print(f"Маскировка номера счёта {ACCOUNT_NUMBER_CONST}, результат: {masks.get_mask_account(ACCOUNT_NUMBER_CONST)}")

card_number = input("Введите номер карты для маскировки (16 символов):")
print(f"Замаскированный номер карты: {masks.get_mask_card_number(card_number)}")

account_number = input("Введите номер счёта для маскировки (20 символов):")
print(f"Замаскированный номер счета: {masks.get_mask_account(account_number)}")

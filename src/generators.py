from typing import Dict, Generator, List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Generator:
    "Итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)"
    if not transactions:
        raise ValueError("Список транзакций пуст")
    currency_code_list = []
    source_flag = False  # Флаг источник - json
    for transaction in transactions:
        if "operationAmount" in transaction:
            currency_code_list.append(transaction["operationAmount"]["currency"]["code"])
        else:
            source_flag = True  # Флаг источник - csv или xlsx
            currency_code_list.append(transaction["currency_code"])

    if currency_code not in currency_code_list:
        raise ValueError("Операции с заданной валютой отсутствуют")
    if source_flag:  # Если источник - csv или xlsx
        for transaction in transactions:
            if transaction["currency_code"] == currency_code:
                yield transaction
    else:  # Если источник - json
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == currency_code:
                yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator:
    "Итератор, который поочередно выдает описание каждой транзакции в текстовом формате"
    if not transactions:
        raise ValueError("Список транзакций пуст")
    if "description" not in ["description" for x in transactions if "description" in x]:
        raise ValueError("Описание транзакции отсутствует")
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    "Итератор, который поочередно выдает номер карты в заданном диапазоне от start до stop в текстовом формате"
    card_numbers = ("0" * (16 - len(str(x))) + str(x) for x in range(start, stop + 1))
    for number in card_numbers:
        yield f"{number[0:4]} {number[4:8]} {number[8:12]} {number[12:]}"

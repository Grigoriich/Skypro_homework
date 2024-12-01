from typing import Dict, List, Generator


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Generator:
    "Генераторная функция, возвращающая итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)"
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> str:
    "Генераторная функция, возвращающая итератор, который поочередно выдает описание каждой транзакции в текстовом формате"
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> str:
    "Генераторная функция, возвращающая итератор, который в порядке возрастания выдает номер карты в заданном диапазоне от start до stop в текстовом формате"
    card_numbers = ("0"*(16-len(str(x)))+str(x) for x in range(start, stop+1))
    for number in card_numbers:
        yield f"{number[0:4]} {number[4:8]} {number[8:12]} {number[12:]}"


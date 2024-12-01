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
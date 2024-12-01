from typing import Dict, List, Generator


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Generator:
    "Генераторная функция, возвращающая итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)"
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


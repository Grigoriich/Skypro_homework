import pytest
from src.generators import filter_by_currency

def test_filter_by_currency_usd(transactions, transactions_usd):
    filtered_transaction = filter_by_currency(transactions, "USD")
    for transaction_usd in transactions_usd:
        assert next(filtered_transaction) == transaction_usd


def test_filter_by_currency_rub(transactions, transactions_rub):
    filtered_transaction = filter_by_currency(transactions, "RUB")
    for transaction_rub in transactions_rub:
        assert next(filtered_transaction) == transaction_rub
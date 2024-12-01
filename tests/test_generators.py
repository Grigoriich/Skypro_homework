import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency_usd(transactions, transactions_usd):
    filtered_transaction = filter_by_currency(transactions, "USD")
    for transaction_usd in transactions_usd:
        assert next(filtered_transaction) == transaction_usd


def test_filter_by_currency_rub(transactions, transactions_rub):
    filtered_transaction = filter_by_currency(transactions, "RUB")
    for transaction_rub in transactions_rub:
        assert next(filtered_transaction) == transaction_rub


def test_transaction_descriptions(transactions, fix_descriptions):
    transaction_description = transaction_descriptions(transactions)
    for description in fix_descriptions:
        assert next(transaction_description) == description


def test_card_number_generator():
    card_number = card_number_generator(9999, 10009)
    assert next(card_number) == "0000 0000 0000 9999"
    assert next(card_number) == "0000 0000 0001 0000"
    assert next(card_number) == "0000 0000 0001 0001"
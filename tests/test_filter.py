import pytest

from src.filter import filter_by_string, counter_by_category_list
from tests.conftest import counted_descriptions


def test_filter_by_string(transactions):
    assert filter_by_string(transactions, "организац") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_filter_by_string_empty_pattern(transactions):
    assert filter_by_string(transactions, "") == transactions


def test_filter_by_string_without_description(transactions_without_description):
    assert filter_by_string(transactions_without_description, "орг") == [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_counter_by_category_list(transactions_without_description, fix_descriptions, counted_descriptions):
    assert counter_by_category_list(transactions_without_description, fix_descriptions) == counted_descriptions


def test_counter_by_empty_category_list(transactions_without_description, counted_descriptions):
    assert counter_by_category_list(transactions_without_description, []) == {}

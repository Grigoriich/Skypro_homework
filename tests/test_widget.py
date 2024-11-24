import pytest
from black import datetime

from src.widget import get_date, get_date_format, mask_account_card


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Visa Gold 8990922113665229", "Visa Gold 8990 92** **** 5229"),
    ],
)
def test_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize(
    "card_number", [("123"), (""), ("11112222333344445555"), ("1111222233334444"), ("Azazaz hehe 1111222233334444")]
)
def test_invalid_account_card(card_number):
    with pytest.raises(ValueError):
        mask_account_card(card_number)


def test_wrong_type_account_card(wrong_type_fixture):
    with pytest.raises(TypeError):
        mask_account_card(wrong_type_fixture)


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-25T02:26:18.671407", "25.03.2024"),
        ("2023-02-20T02:26:18.671407", "20.02.2023"),
        ("2022-01-15T02:26:18.671407", "15.01.2022"),
    ],
)
def test_get_date(input_date, expected):
    assert get_date(input_date) == expected


@pytest.mark.parametrize(
    "input_date",
    [
        ("123"),
        (""),
        ("Azazaz-hehe-1111222233334444"),
        ("AAAA-0F-2L"),
        ("2024-02-2"),
        ("2024-02-2K"),
        ("202-02-20"),
        ("2024-2-20"),
    ],
)
def test_invalid_date(input_date):
    with pytest.raises(ValueError):
        get_date(input_date)


def test_wrong_type_date(wrong_type_fixture):
    with pytest.raises(TypeError):
        get_date(wrong_type_fixture)


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-25T02:26:18.671407", datetime(2024, 3, 25)),
        ("2023-02-20T02:26:18.671407", datetime(2023, 2, 20)),
        ("2022-01-15T02:26:18.671407", datetime(2022, 1, 15)),
    ],
)
def test_get_date_format(input_date, expected):
    assert get_date_format(input_date) == expected


@pytest.mark.parametrize(
    "input_date",
    [
        ("123"),
        (""),
        ("Azazaz-hehe-1111222233334444"),
        ("AAAA-0F-2L"),
        ("2024-02-2"),
        ("2024-02-2K"),
        ("202-02-20"),
        ("2024-2-20"),
    ],
)
def test_invalid_date_format(input_date):
    with pytest.raises(ValueError):
        get_date_format(input_date)


def test_wrong_type_date_format(wrong_type_fixture):
    with pytest.raises(TypeError):
        get_date_format(wrong_type_fixture)

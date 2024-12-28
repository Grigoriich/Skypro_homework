import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_transaction_amount_in_rub

load_dotenv("../.env")
apilayer_token = os.getenv("API_KEY")


def test_get_transaction_amount_in_rub():
    assert (
        get_transaction_amount_in_rub(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "RUB", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == 8221.37
    )


@patch("requests.get")
def test_get_transaction_amount_in_rub_from_usd(mock_get):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 1},
        "info": {"timestamp": 1735324217, "rate": 105.748544},
        "date": "2024-12-27",
        "result": 105.748544,
    }
    assert (
        get_transaction_amount_in_rub(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == 105.748544
    )
    mock_get.assert_called_once_with(
        f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={'USD'}&amount={'8221.37'}",
        headers={"apikey": apilayer_token},
    )

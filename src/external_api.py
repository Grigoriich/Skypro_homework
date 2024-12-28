import os

import requests
from dotenv import load_dotenv

load_dotenv("../.env")

apilayer_token = os.getenv("API_KEY")


def get_transaction_amount_in_rub(transaction: dict) -> float:
    "Функция, возвращающая сумму в рублях по переданной транзакции"
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        headers = {"apikey": apilayer_token}
        r = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from="
            f"{transaction['operationAmount']['currency']['code']}&amount={transaction['operationAmount']['amount']}",
            headers=headers,
        )
        return r.json()["result"]

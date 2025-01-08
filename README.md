# Проект "Виджет банковских операций клиента"

## Описание:

Проект "Виджет банковских операций клиента" - это виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка:

1. Клонируйте репозиторий:

```
git clone https://github.com/Grigoriich/Skypro_homework.git
```


## Использование:

1. Виджет содержит функции:
- mask_account_card: возвращает замаскированный номер карты или счета с типом номера. Пример работы функции:
```
#Ввод:
print(mask_account_card("Visa Platinum 7000792289606361"))
#Вывод:
Visa Platinum 7000 79** **** 6361
```
- get_date: возвращает дату в формате "ДД.ММ.ГГГГ" из формата "2019-07-03T18:35:29.512364". Пример работы функции:
```
#Ввод:
print(get_date("2019-07-03T18:35:29.512364"))
#Вывод:
03.07.2019
```
- get_date_format: возвращает дату в формате datetime из формата "2019-07-03T18:35:29.512364" для сортировки по дате. Пример работы функции:
```
#Ввод:
print(get_date_format("2019-07-03T18:35:29.512364"))
#Вывод:
2019-07-03 00:00:00
```
- filter_by_state: фильтрует список словарей по ключу state. Пример работы функции:
```
#Ввод:
print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
#Вывод:
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
- sort_by_date: сортирует список словарей по дате, с возможностью изменения порядка сортировки. Пример работы функции:
```
#Ввод:
print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
#Вывод:
[{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
```

- filter_by_currency: генераторная функция, которая поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD). Пример работы функции:
```
#Ввод:
a = filter_by_currency(transactions, "RUB")
Где transactions:
    [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        })
        
print(next(a))

#Вывод:
{
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160",
}
```

- transaction_descriptions: генераторная функция, которая поочередно выдает описание каждой транзакции в текстовом формате. Пример работы функции:
```
#Ввод:
a = transaction_descriptions(transactions)
Где transactions:
    [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        })
print(next(a))
print(next(a))
print(next(a))
#Вывод:
"Перевод организации"
"Перевод со счета на счет"
"Перевод со счета на счет"
```

- card_number_generator: генераторная функция, которая поочередно выдает номер карты в заданном диапазоне от start до stop в текстовом формате XXXX XXXX XXXX XXXX. Пример работы функции:
```
#Ввод:
a = card_number_generator(9999, 10001)
print(next(a))
print(next(a))
print(next(a))
#Вывод:
"0000 0000 0000 9999"
"0000 0000 0001 0000"
"0000 0000 0001 0001"
```

- log: декоратор, который логирует успешность выполнения функции в консоль или файл. Пример работы функции:
```
#Ввод:
@log(filename=None)
def multiply(x, y):
    return x * y
multiply(2, 3)
#Вывод:
"multiply ok\n"

#Ввод:
@log(filename="result.txt")
def multiply(x, y):
    raise ValueError("Недопустимые значения")

multiply(2, 3)
with open("text.txt", "r") as file:
    content = file.readlines()
    print(content[-1])
#Вывод:
"multiply error: Недопустимые значения. Inputs: (2, 3), {}\n"
```

- load_json_from_path: функция, возвращающая список словарей из json файла по указанному пути. Пример работы функции:
```
#Ввод:
json_data = load_json_from_path("../data/operations.json")
print(json_data[0])
#Вывод:
{
  "id": 441945886,
  "state": "EXECUTED",
  "date": "2019-08-26T10:50:58.294041",
  "operationAmount": {
    "amount": "31957.58",
    "currency": {
      "name": "руб.",
      "code": "RUB"
    }
  },
  "description": "Перевод организации",
  "from": "Maestro 1596837868705199",
  "to": "Счет 64686473678894779589"
}
```

- get_transaction_amount_in_rub: функция, возвращающая сумму в рублях по переданной транзакции. Пример работы функции:
```
#Ввод:
json_data = load_json_from_path("../data/operations.json")
example = get_transaction_amount_in_rub(json_data[1])
print(example)
#Вывод:
869206.932982
```

- import_from_csv: функция, импортирующая финансовые операции из csv и возвращающая список словарей. Пример работы функции:
```
#Ввод:
data = import_from_csv("../data/transactions.csv")
print(data)
#Вывод:
[{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]
```

- import_from_xlsx: функция, импортирующая финансовые операции из xlsx и возвращающая список словарей. Пример работы функции:
```
#Ввод:
data = import_from_xlsx("../data/transactions_excel.xlsx")
print(data)
#Вывод:
[{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]
```

## Тестирование:

Тестирование функционала осуществляется в пакете "tests".
Все функции протестированы на все возможные входные данные с учетом некорректных вариантов.
from src.filter import filter_by_string
from src.generators import filter_by_currency
from src.import_from_csv_xlsx import import_from_csv, import_from_xlsx
from src.processing import filter_by_state, sort_by_date
from src.utils import load_json_from_path
from src.widget import get_date, mask_account_card


def main():
    print(
        """Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )
    points_list = [
        "Для обработки выбран JSON-файл\n",
        "Для обработки выбран CSV-файл\n",
        "Для обработки выбран XLSX-файл\n",
    ]
    point = int(input())
    while point not in range(1, 4):
        print(
            """Выбран несуществующий пункт.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
        )
        point = int(input())
    print(points_list[point - 1])

    # пути с данными из примера
    paths_to_operations = ["../data/operations.json", "../data/transactions.csv", "../data/transactions_excel.xlsx"]

    print("Введите путь к файлу (0 - для выбора данных из примера):")
    path_to_data = input()
    if path_to_data == "0":
        path_to_data = paths_to_operations[point - 1]
    import_operations = [load_json_from_path, import_from_csv, import_from_xlsx]

    operations_list = import_operations[point - 1](path_to_data)  # загруженный список словарей

    print(
        """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    )
    status_list = ["EXECUTED", "CANCELED", "PENDING"]
    status = input().upper()
    while status not in status_list:
        print(
            f"""Статус операции '{status}' недоступен.
\nВведите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        status = input().upper()

    operations_list = filter_by_state(operations_list, status)
    print(f"Операции отфильтрованы по статусу {status}")

    print("Отсортировать операции по дате? Да/Нет")
    answer = input().lower()
    while answer not in ["да", "нет"]:
        print("Некорректный ввод. Отсортировать операции по дате? Да/Нет")
        answer = input().lower()

    if answer == "да":
        print("Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию")
        direction = input().lower()
        while direction not in ["по возрастанию", "по убыванию"]:
            print("Некорректный ввод. Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию")
            direction = input().lower()
        if direction == "по возрастанию":
            operations_list = sort_by_date(operations_list)
        else:
            operations_list = sort_by_date(operations_list, False)

    print("Выводить только рублевые транзакции? Да/Нет")
    answer = input().lower()
    while answer not in ["да", "нет"]:
        print("Некорректный ввод. Выводить только рублевые тразакции? Да/Нет")
        answer = input().lower()
    if answer == "да":
        operations_list = [operation for operation in filter_by_currency(operations_list, "RUB")]

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    answer = input().lower()
    while answer not in ["да", "нет"]:
        print("Некорректный ввод. Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        answer = input().lower()
    if answer == "да":
        print("Введите слово для поиска")
        search_key = input()
        operations_list = filter_by_string(operations_list, search_key)

    print("Распечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(operations_list)}")

    for operation in operations_list:
        oper_descr = operation["description"]
        print(f"\n{get_date(operation["date"])} {oper_descr}")
        if "перевод" not in oper_descr.lower():
            print(mask_account_card(operation["to"]))
        else:
            print(f"{mask_account_card(operation["from"])} -> {mask_account_card(operation["to"])}")

        if point == 1:  # Если импорт из JSON
            print(
                f"Сумма: {operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}"
            )
        else:  # Если импорт из csv или xlsx
            print(f"Сумма: {operation["amount"]} {operation["currency_name"]}")


if __name__ == "__main__":
    main()

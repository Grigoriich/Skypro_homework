 import pandas as pd

def import_from_csv(path_: str) -> list:
    """Функция, импортирующая финансовые операции из csv и возвращающая список словарей"""
    result = pd.read_csv(path_, delimiter=";")
    result = result.to_dict(orient="records")
    return result


def import_from_xlsx(path_: str) -> list:
    """Функция, импортирующая финансовые операции из xlsx и возвращающая список словарей"""
    result = pd.read_excel(path_)
    result = result.to_dict(orient="records")
    return result


if __name__ == "__main__":
    result = import_from_csv("../data/transactions.csv")
    print(result[:3])
    print(type(result))
    res = import_from_xlsx("../data/transactions_excel.xlsx")
    print(res[:3])
    print(type(res))

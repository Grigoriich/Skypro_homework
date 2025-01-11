from typing import Dict, List

import pandas as pd


def import_from_csv(path_: str) -> List[Dict]:
    """Функция, импортирующая финансовые операции из csv и возвращающая список словарей"""
    result = pd.read_csv(path_, delimiter=";")
    result = result.to_dict(orient="records")
    return result


def import_from_xlsx(path_: str) -> List[Dict]:
    """Функция, импортирующая финансовые операции из xlsx и возвращающая список словарей"""
    result = pd.read_excel(path_)
    result = result.to_dict(orient="records")
    return result

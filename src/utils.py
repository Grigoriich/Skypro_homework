import json


def load_json_from_path(path_: str) -> list:
    "Функция, возвращающая список словарей из json файла по указанному пути"
    try:
        with open(path_, encoding="utf-8") as j:
            json_data = json.load(j)
        return json_data
    except Exception:
        return []

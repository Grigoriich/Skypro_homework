import json
import logging


utils_logger = logging.getLogger(__name__)
utils_file_handler = logging.FileHandler("../logs/utils.log", mode="w")
utils_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
utils_file_handler.setFormatter(utils_formatter)
utils_logger.addHandler(utils_file_handler)
utils_logger.setLevel(logging.DEBUG)


def load_json_from_path(path_: str) -> list:
    "Функция, возвращающая список словарей из json файла по указанному пути"
    try:
        utils_logger.info(f"Загрузка json файла из пути {path_}")
        with open(path_, encoding="utf-8") as j:
            json_data = json.load(j)
        utils_logger.info("json файл успешно десериализован")
        return json_data
    except Exception as e:
        utils_logger.error(f"Произошла ошибка: {e}", exc_info=True)
        return []

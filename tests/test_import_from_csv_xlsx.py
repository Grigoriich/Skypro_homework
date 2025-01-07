from unittest.mock import Mock

import pandas as pd

from src.import_from_csv_xlsx import import_from_csv, import_from_xlsx


def test_import_from_csv():
    mock_import_csv = Mock(
        return_value=pd.DataFrame([{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}])
    )
    pd.read_csv = mock_import_csv
    assert import_from_csv("../data/transactions.csv") == [
        {"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}
    ]
    mock_import_csv.assert_called_once_with("../data/transactions.csv", delimiter=";")


def test_import_from_xlsx():
    mock_import_xlsx = Mock(
        return_value=pd.DataFrame([{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}])
    )
    pd.read_excel = mock_import_xlsx
    assert import_from_xlsx("../data/transactions_excel.xlsx") == [
        {"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}
    ]
    mock_import_xlsx.assert_called_once_with("../data/transactions_excel.xlsx")

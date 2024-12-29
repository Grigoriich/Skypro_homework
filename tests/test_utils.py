from unittest.mock import patch

from src.utils import load_json_from_path


@patch("builtins.open", create=True)
def test_load_json_from_file(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = '[{"id": 441945886}]'
    assert load_json_from_path("../data/operations.json") == [{"id": 441945886}]
    mock_open.assert_called_once_with("../data/operations.json", encoding="utf-8")


@patch("builtins.open", create=True)
def test_load_json_from_empty_file(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = None
    assert load_json_from_path("../data/operations.json") == []
    mock_open.assert_called_once_with("../data/operations.json", encoding="utf-8")

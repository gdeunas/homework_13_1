from unittest.mock import MagicMock, patch

from src.import_data import read_csv, read_xl


@patch("pandas.read_csv")
def test_read_csv_success(mock_read_csv):
    """test read csv success"""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    mock_read_csv.return_value = mock_df

    result = read_csv("some.csv")

    mock_read_csv.assert_called_once_with("some.csv", delimiter=";")
    assert result == [{"a": 1, "b": 2}, {"a": 3, "b": 4}]


@patch("pandas.read_csv")
def test_read_csv_exception(mock_read_csv):
    """test read csv exception"""
    mock_read_csv.side_effect = Exception("file error")
    result = read_csv("some.csv")
    mock_read_csv.assert_called_once_with("some.csv", delimiter=";")
    assert result == []


@patch("pandas.read_excel")
def test_read_xl_success(mock_read_excel):
    """test read xl success"""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {"col1": "val1", "col2": "val2"},
        {"col1": "val3", "col2": "val4"},
    ]
    mock_read_excel.return_value = mock_df

    result = read_xl("some.xlsx")

    mock_read_excel.assert_called_once_with("some.xlsx")
    assert result == [
        {"col1": "val1", "col2": "val2"},
        {"col1": "val3", "col2": "val4"},
    ]


@patch("pandas.read_excel")
def test_read_xl_exception(mock_read_excel):
    """test read xl exception"""
    mock_read_excel.side_effect = Exception("file error")
    result = read_xl("some.xlsx")
    mock_read_excel.assert_called_once_with("some.xlsx")
    assert result == []

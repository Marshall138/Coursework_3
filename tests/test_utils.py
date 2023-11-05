import json
from unittest.mock import mock_open, patch

from src.utils import *

def test_load_operations(operations_mocked_data):
    mocked_json_data = json.dumps(operations_mocked_data)
    m = mock_open(read_data=mocked_json_data)
    with patch("builtins.open", m):
        result = load_operations()
    assert result == operations_mocked_data

#    with open('src.operations.json' "r", encoding="utf-8") as file:
#        data = json.load(file)
#        data_dict = []
#        for list_data in data:
#            data_dict.append(list_data)
#
#        assert datas == data_dict


def test_remove_items(operations_mocked_data, remove_mocked_data):
    assert remove_items(operations_mocked_data) == remove_mocked_data


def test_sort_key(dict_test):
    assert sort_key(dict_test) == "2019-08-26T10:50:58.294041"


def test_sort_datas(remove_mocked_data, mocked_data_sort):
    assert sort_datas(remove_mocked_data) == mocked_data_sort


def test_executed_operations(mocked_data_sort, mocked_result_data):
    assert executed_operations(mocked_data_sort) == mocked_result_data


def test_number_operation(mocked_result_data, mocked_number_last_data):
    assert number_operation(mocked_result_data, 5) == mocked_number_last_data


def test_get_result(operations_mocked_data, remove_mocked_data, mocked_data_sort, mocked_result_data,
                         mocked_number_last_data):
    with patch("src.utils.load_operations", return_value=operations_mocked_data):
        with patch("src.utils.remove_items", return_value=remove_mocked_data):
            with patch("src.utils.sort_datas", return_value=mocked_data_sort):
                with patch("src.utils.executed_operations", return_value=mocked_result_data):
                    with patch("src.utils.number_operation", return_value=mocked_number_last_data):
                        result = get_result(5)
                        assert result == mocked_number_last_data

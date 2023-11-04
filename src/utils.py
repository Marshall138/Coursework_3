import json


def load_operations():
    """
    Открываем json файл
    :return:
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def remove_items(data):
    """
    Удаление пустых элементов из списка
    :return:
    """
    return [item for item in data if "date" in item]


def sort_key(date):
    """
    Ключ для сортировки файла по дате
    :param date:
    :return:
    """
    return date["date"]


def sort_datas(data):
    """
    Сортировка данных по дате
    :return:
    """
    data.sort(reverse=True, key=sort_key)
    return data


def executed_operations(data):
    """
    Фильтрация данных по EXECUTED
    :return:
    """
    return [exe for exe in data if exe["state"] == "EXECUTED"]




def number_operation(data, number):
    """
    Возвращает number
    :param data:
    :param number:
    :return:
    """
    return data[:number]


def get_result(number):
    """
    Подготовка результата для вывода
    :param number:
    :return:
    """
    get_operation = load_operations()
    remove_data = remove_items(get_operation)
    sort_data = sort_datas(remove_data)
    executed_operation = executed_operations(sort_data)
    result_data = number_operation(executed_operation, number)
    return result_data


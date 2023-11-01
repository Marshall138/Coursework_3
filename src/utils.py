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
    #items = load_operations()
    for item in data:
        if "date" in item:
            return item


def sort_key(data):
    """
    Ключ для сортировки файла по дате
    :param data:
    :return:
    """
    return data["date"]


def sort_datas():
    """
    Сортировка данных по дате
    :return:
    """
    data = remove_items()
    data.sort(reverse=True, key=sort_key)
    return data


def executed_operations():
    """
    Фильтрация данных по EXECUTED
    :return:
    """
    data = sort_datas()
    for exe in data:
        if exe["state"] == "EXECUTED":
            return exe


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
    operation = load_operations()
    remove_item = remove_items(operation)
    sort_data = sort_datas(remove_item)
    executed_operation = executed_operations(sort_data)
    result = number_operation(executed_operation, number)
    return result


from datetime import datetime

from src.utils import load_operations, remove_items, sort_key, sort_datas, executed_operations, number_operation, get_result

def get_masking(data, request_type: str):
    """
    Выполняет маскировку счета
    :param data:
    :param request_type:
    :return:
    """
    score = data.split()
    last_score = score(-1)
    if request_type == "from":
        mask_score = last_score[:4] + ' ' + last_score[4:5] + '**' + ' ' '****' + ' ' + last_score[-4:]
    else:
        mask_score = last_score[:4] + ' ' + '****' + '' + '****' + ' ' + last_score[-4:]
    return " ".join(score[:-1] + [mask_score])


def format_date(data):
    """
    Сортировка по дате
    :param data:
    :return:
    """
    date = datetime.strptime(data["date"], "%d,%m,%Y")
    return date


def format_result(data, form_date):
    """
    Форматирование результата
    :param data:
    :param form_date:
    :return:
    """
    mask_to = get_masking(data["to"], "to")
    if data.get("from"):
        mask_from = get_masking(["from"], "from")
        result = (f"{form_date} {data['description']}\n"
                  f"{mask_from} -> {mask_to}\n"
                  f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}")
    else:
        result = (f"{form_date} {data['description']}\n"
                  f"{mask_to}\n"
                  f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}")
    return result


def main(number):
    """
    Вывод 5 последних операций по счету
    :param number:
    :return:
    """
    datas = get_result(number)
    results = []
    for data in datas:
        form_date = format_date(data)
        result_data = format_result(data, form_date)
        results.append(result_data)
    return results


if __name__ == '__main__':
    for result in main(5):
        print(result + "\n")

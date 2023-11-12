from datetime import datetime

from src.utils import *

def get_masking(data, request_type: str):
    """
    Выполняет маскировку счета
    :param data:
    :param request_type:
    :return:
    """
    score = data.split()
    last_score = score[-1]
    if request_type == "from":
        mask_score = f"{last_score[:4]} {last_score[4:6]}** **** {last_score[-4:]}"

    else:
        mask_score = f"**{last_score[-4:]}"
        #mask_score = f"Неизвестно -> **{last_score[-4:]}"
    return " ".join(score[:-1] + [mask_score])


def format_date(data):
    """
    Сортировка по дате
    :param data:
    :return:
    """
    date_o = datetime.strptime(data["date"], "%Y-%m-%dT%H:%M:%S.%f")
    return date_o.strftime("%d.%m.%Y")


def format_result(data, form_date, mask_to, mask_from=None):
    """
    Форматирование результата
    :param data:
    :param form_date:
    :param mask_to:
    :param mask_from:
    :return:
    """
    description = f"{form_date} {data['description']}"
    transaction = mask_from and f"{mask_from} -> {mask_to}" or mask_to
    amount = f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}"
    return f"{description}\n{transaction}\n{amount}"


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
        mask_to = get_masking(data['to'], "to")
        mask_from = None
        if "from" in data:
            mask_from = get_masking(data['from'], "from")
        result_data = format_result(data, form_date, mask_to, mask_from)
        results.append(result_data)
    return results


if __name__ == '__main__':
    for result in main(5):
        print(result + "\n")


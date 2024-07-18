from __future__ import annotations

import json
import datetime


def get_data_json(file_name) -> list:
    with open(file_name, 'r', encoding="utf-8") as file:
        return json.load(file)


def sort_status(json_list: list, state: str) -> list:
    result = []
    for i in json_list:
        if i.get('state') == state:
            result.append(i)
    return result


def sort_dates(list_: list) -> list:
    return sorted(list_, key=lambda x: x['date'])


def revers(list_: list) -> list:
    return list_[::-1]


def format_date(value: str) -> str:
    date = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
    return date.strftime('%d.%m.%Y')


def get_from_to(dict_: dict, from_: str, to_: str) -> (bool, str):
    from_transaction = dict_.get(from_)
    to_transaction = dict_.get(to_)
    if from_transaction is None:
        return False, to_transaction
    return from_transaction, to_transaction


def cipher(str_: str | bool) -> str | None:

    if not str_:
        return None
    elif "счет" in str_.lower():
        _name = str_.split()[:-1]
        _number = str_.split()[-1]
        result = f"{' '.join(_name)} **{_number[-4:]}"
        return result
    else:
        card_name = str_.split()[:-1]
        card_number = str_.split()[-1]
        result = f"{' '.join(card_name)} {card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        return result
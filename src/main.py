from src.function import (
    get_data_json,
    sort_status,
    sort_dates,
    revers,
    format_date,
    get_from_to,
    cipher
)
from src.config import data_file_name


def main():
    list_data = get_data_json(data_file_name)
    list_sorted_status = sort_status(list_data, state="EXECUTED")
    list_sorted_dates = sort_dates(list_sorted_status)
    last_5_transaction = revers(list_sorted_dates[-5:])
    for i in last_5_transaction:
        print(f"{format_date(i['date'])} {i.get('description')}")
        from_transaction, to_transaction = get_from_to(i, from_='from', to_='to')
        if from_transaction:
            print(f"{cipher(from_transaction)} -> {cipher(to_transaction)}")
        else:
            print(f"{cipher(to_transaction)}")
        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
        print()


if __name__ == "__main__":
    main()

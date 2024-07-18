from src.function import sort_status
from src.function import sort_dates
from src.function import revers
from src.function import format_date
from src.function import get_from_to
from src.function import cipher


def test_sor_status():
    t_list = [
        {'state': 'test'},
        {'state': 'test_1'}
    ]
    assert sort_status(json_list=t_list, state='test') == [{'state': 'test'}]


t_list_date = [
        {'date': 'date": "2019-08-26T10:50:58.294041'},
        {'date': '2018-12-20T16:43:26.929246'}
]


def test_sort_dates():
    assert sort_dates(list_=t_list_date) == [{'date': '2018-12-20T16:43:26.929246'},
                                             {'date': 'date": "2019-08-26T10:50:58.294041'}
                                             ]


def test_revers():
    assert revers(list_=t_list_date) == [{'date': '2018-12-20T16:43:26.929246'},
                                         {'date': 'date": "2019-08-26T10:50:58.294041'}
                                         ]


def test_format_date():
    assert format_date(value='2019-08-26T10:50:58.294041') == '26.08.2019'


def test_get_from_to():
    t_dict = {'from': 'Счет 10848359769870775355',
              'to': 'Счет 21969751544412966366'}
    t_dict_1 = {'to': 'Счет 21969751544412966366'}
    assert get_from_to(dict_=t_dict, from_='from', to_='to') == ('Счет 10848359769870775355',
                                                                 'Счет 21969751544412966366')
    assert get_from_to(dict_=t_dict_1, from_='from', to_='to') == (False, 'Счет 21969751544412966366')


def test_cipher():
    assert cipher(str_='Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658'
    assert cipher(str_='Счет 21969751544412966366') == 'Счет **6366'
    assert cipher(str_=False) is None
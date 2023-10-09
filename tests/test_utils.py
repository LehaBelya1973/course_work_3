import json

from config import FILE_NAME
from src.utils import get_date, mask_card_number, mask_account_number, mask_prepare_message_number, filter_and_sorting, \
    prepare_user_message


def test_get_date():
    assert get_date("2018-03-23T10:45:06.972075") == "23.03.2018"


def test_mask_card_number():
    assert mask_card_number("7158300734726758") == "7158 30** **** 6758"


def test_mask_account_number():
    assert mask_account_number("35383033474447895560") == "**5560"


def test_mask_prepare_message_number():
    assert mask_prepare_message_number("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_prepare_message_number("Счет 75106830613657916952") == "Счет **6952"
    assert mask_prepare_message_number("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"


def test_prepare_user_message():
    with open(FILE_NAME) as file:
        data = json.load(file)

    items = filter_and_sorting(data)
    data_test = """08.12.2019 Открытие вклада
Личный счет -> Счет **5907
41096.24 USD
"""
    assert prepare_user_message(items[0]) == data_test

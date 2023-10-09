from src.utils import get_date, mask_card_number, mask_account_number, mask_prepare_message_number


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

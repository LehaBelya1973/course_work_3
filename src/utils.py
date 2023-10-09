def filter_and_sorting(data: list):
    """Функция отсортировывает по дате и выполнению операции"""
    items = [item for item in data if item.get('state') == "EXECUTED"]
    items.sort(key=lambda x: x.get('date'), reverse=True)
    return items


def get_date(date: str):
    """Функция преобразует дату в необходимый формат через точку (dd.mm.YYYY)"""
    date_num = date[0:10].split('-')
    return date_num[2] + '.' + date_num[1] + '.' + date_num[0]


def mask_prepare_message_number(message):
    """Будет определять карта или счет"""
    if message is None:
        return 'Личный счет'

    message_split = message.split(' ')
    if message_split[0] == 'Счет':
        hidden_number = mask_account_number(message_split[-1])
    else:
        hidden_number = mask_card_number(message_split[-1])

    return ' '.join(message_split[:-1]) + ' ' + hidden_number


def mask_card_number(number: str):
    """Функция проверяет, что номер карты состоит из 16 цифр и
    маскирует части номера карты"""
    if number.isdigit() and len(number) == 16:
        return number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]
    else:
        print('Номер карты не подходит')


def mask_account_number(number: str):
    """Функция проверяет, что счет состоит из цифр и маскирует
    часть счета, выводы четыре последние цифры"""
    if number.isdigit() and len(number) >= 4:
        return "**"+number[-4:]
    else:
        print('номер счета не подходит')


def prepare_user_message(item: dict):
    """Функция собирает всю информацию и выводит согласно
    заданию"""
    date = get_date(item.get('date'))
    desc = item.get('description')
    from_ = mask_prepare_message_number(item.get('from'))
    to_ = mask_prepare_message_number(item.get('to'))
    amount = item.get('operationAmount').get('amount')
    curr = item.get('operationAmount').get('currency').get('name')

    return f'{date} {desc}\n{from_} -> {to_}\n{amount} {curr}\n'

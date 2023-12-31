import json
from config import FILE_NAME
from src.utils import filter_and_sorting, prepare_user_message


def main():
    """Функция забирает информацию из .json, подготавливает и
    выводит последние пять операций"""

    with open(FILE_NAME) as file:
        data = json.load(file)

    items = filter_and_sorting(data)

    for i in range(5):
        print(prepare_user_message(items[i]))


main()

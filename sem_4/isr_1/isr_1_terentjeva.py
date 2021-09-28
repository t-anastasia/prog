from prettytable import PrettyTable
import json


def create_table(data):
    table = PrettyTable()
    table.field_names = ["Name", "Sell", "Buy"]
    for item in data:
        table.add_row([item['name'], item['sell'], item['buy']])
    return table


def main():
    try:
        data = json.load(open('data.json'))
    except(FileNotFoundError):
        print("Такой таблицы не существует.")
    else:
        print(create_table(data))


main()
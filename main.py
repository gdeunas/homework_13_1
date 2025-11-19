from pathlib import Path

from src.import_data import read_csv, read_xl


def main():
    """main func"""
    current_file = Path(__file__).resolve()
    directory = current_file.parent
    file_csv = directory / 'data' / 'transactions.csv'
    file_xl = directory / 'data' / 'transactions_excel.xlsx'

    print(read_csv(file_csv))

    print(read_xl(file_xl))


main()

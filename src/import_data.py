import pandas as pd
import csv


def read_csv(file_csv):
    """функция для считывания финансовых операций из CSV."""
    readed_csv = []
    try:
        df = pd.read_csv(file_csv)
        return df
        # with open(file_csv) as file:
        #     reader = csv.DictReader(file)
        #     for row in reader:
        #         readed_csv.append(row)
        #     print(type(readed_csv))
    except Exception as e:
        print(e)
    # finally:
    #     return readed_csv


def read_xl(file_xl):
    """функция для считывания финансовых операций из Excel."""
    excel_data = pd.read_excel(file_xl)
    return excel_data

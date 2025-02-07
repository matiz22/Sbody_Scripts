import pandas as pd


class ExcelManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        return pd.read_excel(self.file_path)

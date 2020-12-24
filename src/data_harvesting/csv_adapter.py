from config import CSV_FILE_NAME, CSV_FILE_PATH
from data_harvesting.record import LABELS
import pandas as pd
import os


class CSVAdapter:

    def __init__(self):

        self._complete_path = os.path.join(CSV_FILE_PATH, CSV_FILE_NAME)
        self.establish_df()

    def check_csv_exists(self):
        return os.path.isfile(self._complete_path)

    def load_existing_data(self):
        df = pd.read_csv(filepath_or_buffer=self._complete_path)
        return df

    def establish_df(self):

        if self.check_csv_exists():
            self._df = self.load_existing_data()
        else:
            self._df = pd.DataFrame(columns=LABELS)

    def add_record(self, record):
        self._df = self._df.append(record, ignore_index=True)

    def dump_to_csv(self):
        self._df.to_csv(self._complete_path, index=False)
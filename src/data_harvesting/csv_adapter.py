from config import CSV_FILE_NAME, CSV_FILE_PATH
from data_harvesting.record import LABELS
import pandas as pd
import os


class CSVAdapter:
    """CSV adapter for metadata persistance and easy access
    """

    def __init__(self):
        """Constructor
        """
        self._complete_path = os.path.join(CSV_FILE_PATH, CSV_FILE_NAME)
        self.establish_df()

    def check_csv_exists(self):
        """Checks if the CSV file exists

        Returns:
            bool: Whether the file exists
        """
        return os.path.isfile(self._complete_path)

    def load_existing_data(self):
        """Loads CSV file into memory as DataFrame object

        Returns:
            DataFrame: DataFrame of the CSV file
        """
        df = pd.read_csv(filepath_or_buffer=self._complete_path)
        return df

    def establish_df(self):
        """Abstraction function for giving DataFrame back whether it
        is a fresh Dataframe or one that is loaded with existing CSV data.
        """
        if self.check_csv_exists():  # load csv if exists
            self._df = self.load_existing_data()
        else:  # create new CSV otherwise
            self._df = pd.DataFrame(columns=LABELS)

    def add_record(self, record):
        """Adds record to dataframe

        Args:
            record (dict): Record following all correct LABELS keys
        """
        self._df = self._df.append(record, ignore_index=True)

    def dump_to_csv(self):
        """Dumps csv into a file
        """
        self._df.to_csv(self._complete_path, index=False)

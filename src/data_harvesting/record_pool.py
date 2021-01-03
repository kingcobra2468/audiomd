from data_harvesting.record import Record
from data_harvesting.csv_adapter import CSVAdapter
from config import MAX_WORKERS, CSV_FILE_NAME, CSV_FILE_PATH
from concurrent.futures import ThreadPoolExecutor, as_completed


class RecordPool:
    """Record pool wrapper for threaded execution of dataset generation
    """
    def __init__(self, url_list):
        """Constructor

        Args:
            url_list (list): List of urls
        """
        self._create_records(url_list)
        self._csv_adapter = CSVAdapter()

    def _create_records(self, url_list):
        """Creates all of the record objects

        Args:
            url_list (list): List of all Urls
        """
        self._records = [Record(url) for url in url_list]

    def start_job(self):
        """Start the Multithreaded job.
        """
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_records = {executor.submit(
                record.get_meta_row): record for record in self._records}

            for future in as_completed(future_records):
                try: # if a successful completion of record data fetch
                    self._csv_adapter.add_record(future.result())
                except Exception as e:
                    print(str(e))

    def dump_data(self):
        """Wrapper for dumping record data into CSV
        """
        self._csv_adapter.dump_to_csv()
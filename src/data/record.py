from scrappers.content.content_factory import ContentFactory
from scrappers.metadata.metadata_factory import MetadataFactory
from data.utils.csv_utils import gen_uniq_meta_labels
from config import CONTENT_SCRAPPER, METADATA_SCRAPPERS
from collections import Counter


class Record:
    """Dataset record for a new YT entity
    """
    NON_META_LABELS = ['file_name']

    def __init__(self, url, custom_title=None, content_scrapper=CONTENT_SCRAPPER,
                 metadata_scrappers=METADATA_SCRAPPERS):
        """Constructor

        Args:
            url (str): YT url to be downloaded
            base_title (str): Title to be used for Deezer API. Defaults to None
        """
        if not isinstance(content_scrapper, str):
            raise ValueError(f'Unable to set content scrapper as it was defined in the wrong format. ' +
               f'Content scrapper "{content_scrapper}" must be set as a str.')
        if not isinstance(metadata_scrappers, list):
            raise ValueError(f'Unable to set metadata scrappers as it was defined in the wrong format. ' +
                f'Metadata scrapper "{metadata_scrappers}" must be set as a list.')

        self._content_scrapper = ContentFactory.new_instance(content_scrapper)
        self._metadata_scrappers = [MetadataFactory.new_instance(metadata_scrapper)
                                    for metadata_scrapper in metadata_scrappers]
        self._url = url
        self._custom_title = custom_title

    def get_meta_row(self):
        """Generates a metadata csv record for YT entity

        Returns:
            dict: Labeled CSV record
        """
        title = self._content_scrapper.download_entity(self._url).strip()
        title = title if self._custom_title is None else self._custom_title

        meta_csv_row = self.create_empty_row()
        labels_freq = Counter(meta_csv_row.keys())

        meta_csv_row['file_name'] = title  # Populates file_name field

        for metadata_scrapper in self._metadata_scrappers:
            metadata = metadata_scrapper.get_meta_row(title)

            for label, value in metadata.items():
                if label not in labels_freq:  # implies that this label is duplicate and thus has _#
                    raise ValueError(
                        f'Found label "{label}" that doesnt exist in any metadata scrapper.')
                elif labels_freq[label] == 1:
                    meta_csv_row[label] = value
                    continue

                for tag in range(labels_freq[label]):
                    if meta_csv_row[f'label_{tag}'] == '':
                        continue
                    meta_csv_row[f'label_{tag}'] = value
                    return

        return meta_csv_row

    def get_all_labels(self):
        """Returns all labels for a record.

        Returns:
            list: Contains all of the labels/features of the data.
        """
        labels_unique = gen_uniq_meta_labels(
            self._metadata_scrappers) + self.NON_META_LABELS

        return labels_unique

    def create_empty_row(self):
        """Generates an empty CSV record.

        Returns:
            dict: [Empty dict with keys being all LABELS and values being ''
        """
        labels_unique = self.get_all_labels()

        return {label: '' for label in labels_unique}

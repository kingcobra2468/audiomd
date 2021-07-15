from scrappers.content.content_factory import ContentFactory
from scrappers.metadata.metadata_factory import MetadataFactory
from data.utils.csv_utils import gen_uniq_meta_labels
from config import CONTENT_SCRAPPER, METADATA_SCRAPPERS
from collections import Counter


class Record:
    """A complete record of a single YT entity. The entity will be downloaded
    with the chosen content scrapper and appropriate metadata will be generated from
    the configured metadata scrappers.
    """
    NON_META_LABELS = ['file_name', 'youtube_url']

    def __init__(self, url, custom_title=None, content_scrapper=CONTENT_SCRAPPER,
                 metadata_scrappers=METADATA_SCRAPPERS):
        """Constuctor.

        Args:
            url (str): The YT entity that will be downloaded and from which metadata will be
            searched from. 
            custom_title (str, optional): A custom title to override the one automatically pulled
            from the YT entity. Setting a custom title could help metedata generation be more accurate,
            especially if if the YT entity title has phrases like "lyrics", "instrumental" which will
            hinder metadata generation from finding the song. Defaults to None which is equivalent to
            using the automatically pulled YT entity title.
            content_scrapper (str, optional): The Content scrapper to use. Defaults to CONTENT_SCRAPPER
            which is the same as the one set in config.py.
            metadata_scrappers (list(str), optional): The metadata scrappers to use. Defaults to
            METADATA_SCRAPPERS which is the same as the one set in config.py.

        Raises:
            ValueError: Thrown if the chosen content scrapper is not a valid option.
            ValueError: Thrown if one of the metadata scrapper is not a valid option.
        """
        if not isinstance(content_scrapper, str):
            raise ValueError(f'Unable to set content scrapper as it was defined in the wrong format. ' +
                             f'Content scrapper "{content_scrapper}" must be set as a str.')
        if not isinstance(metadata_scrappers, list):
            raise ValueError(f'Unable to set metadata scrappers as it was defined in the wrong format. ' +
                             f'Metadata scrapper "{metadata_scrappers}" must be set as a list.')

        self._content_scrapper = ContentFactory.new_instance(
            content_scrapper.lower())
        self._metadata_scrappers = [MetadataFactory.new_instance(metadata_scrapper.lower())
                                    for metadata_scrapper in metadata_scrappers]
        self._url = url.strip()
        self._custom_title = custom_title.strip()

    def get_meta_row(self):
        """Generates a metadata csv record for a given YT entity.

        Returns:
            dict: Labeled CSV record of metadata and other features.
        """
        title = self._content_scrapper.download_entity(self._url).strip()

        meta_csv_row = self.create_empty_row()
        labels_freq = Counter(meta_csv_row.keys())

        meta_csv_row['file_name'] = title  # Populates file_name field
        meta_csv_row['youtube_url'] = self._url

        # populate the empty row with the appropriate features
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
        """Returns all labels for a record including non-meta and metadata labels.

        Returns:
            list: Contains all of the labels/features of the data.
        """
        labels_unique = gen_uniq_meta_labels(
            self._metadata_scrappers) + self.NON_META_LABELS

        return labels_unique

    def create_empty_row(self):
        """Generates an empty CSV record. from all the labels in the row.

        Returns:
            dict: Empty dict with keys being all LABELS and values being ''.
        """
        labels_unique = self.get_all_labels()

        return {label: '' for label in labels_unique}

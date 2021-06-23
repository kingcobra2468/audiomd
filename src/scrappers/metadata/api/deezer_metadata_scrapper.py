from clients.deezer_client import DeezerClient
from scrappers.base.api.base_api_meta_scrapper import BaseAPIMetaScrapper

class DeezerMetadataScrapper(BaseAPIMetaScrapper):
    """Metascrapper using the Deezer API.
    """
    LABELS = ['artist', 'explicit', 'genre']

    def __init__(self):
        super().__init__(self.LABELS)
        self._deezer_client = DeezerClient()

    def get_meta_row(self, title):
        """Generates a metadata csv record for YT entity.

        Returns:
            dict: Labeled CSV record.
        """
        search_metadata = self._deezer_client.search(title)
        meta_csv_row = self.create_empty_row()
        meta_csv_row['file_name'] = title  # Populates file_name field

        # gets number of returned records from Deezer
        total = search_metadata['total']

        if not total:  # checks if any records exist for Deezer for a search query
            return meta_csv_row

        # naively choose first result
        search_metadata = search_metadata['data'][0]
        record_id = search_metadata['id']

        album_metadata = self._deezer_client.album(record_id)

        self._parse_search_meta(search_metadata, total, meta_csv_row)
        self._parse_album_meta(album_metadata, meta_csv_row)

        return meta_csv_row

    def _parse_search_meta(self, metadata, total, meta_csv_row):
        """Internal parsing of Deezer serch API metadata and record population.

        Args:
            metadata (dict): Deezer JSON response for search query.
            total (int): Number of record responses.
            meta_csv_row (dict): Record for the CSV that is being generated.
        """
        if not total:
            return

        meta_csv_row['artist'] = metadata['artist']['name']
        meta_csv_row['explicit'] = metadata['explicit_lyrics']

    def _parse_album_meta(self, metadata, meta_csv_row):
        """Internal parsing of Deezer album metadata and record population.

        Args:
            metadata (dict): Deezer JSON response for search query.
            meta_csv_row (dict): Record for the CSV that is being generated.
        """
        if 'error' in metadata.keys():  # if no record in api response simply return
            return

        try:  # Attempts to locate the genre name
            meta_csv_row['genre'] = metadata['genres']['data'][0]['name']
        except:
            pass

    def _empty_if_value(self, value, expected_empty):
        """Helper function to check if an API response is an alias to empty.

        Args:
            value (any): The actual value.
            expected_empty (any): Expect value of an empty response value.

        Returns:
            str|any: '' if any otherwise the value itself
        """
        return '' if value == expected_empty else value

    def create_empty_row(self):
        """Generates an empty CSV record from the predefinied scrapper columns.

        Returns:
            dict: Empty dict with keys being all LABELS and values being ''.
        """
        return {label: '' for label in self.LABELS}
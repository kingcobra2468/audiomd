from clients.yt_media_fetcher.yt_media import YTMedia
from clients.metadata_scrapper.deezer_scrapper import DeezerScrapper

# CSV labels
LABELS = ['file_name', 'artist', 'explicit', 'genre']


class Record:
    """Dataset record for a new YT entity
    """

    def __init__(self, url):
        """Constructor

        Args:
            url (str): YT url to be downloaded
        """
        self._yt_media = YTMedia()
        self._deezer_scrapper = DeezerScrapper()
        self._url = url

    def get_meta_row(self):
        """Generates a metadata csv record for YT entity

        Returns:
            dict: Labeled CSV record
        """
        title = self._yt_media.download_entity(self._url).strip()

        search_metadata = self._deezer_scrapper.search(title)
        meta_csv_row = self.create_empty_row()
        meta_csv_row['file_name'] = title  # Populates file_name field

        # gets number of returned records from Deezer
        total = search_metadata['total']

        if not total:  # checks if any records exist for Deezer for a search query
            return meta_csv_row

        # naively choose first result
        search_metadata = search_metadata['data'][0]
        record_id = search_metadata['id']

        album_metadata = self._deezer_scrapper.album(record_id)

        self._parse_search_meta(search_metadata, total, meta_csv_row)
        self._parse_album_meta(album_metadata, meta_csv_row)

        return meta_csv_row

    def _parse_search_meta(self, metadata, total, meta_csv_row):
        """Internal parsing of Deezer serch API metadata and record population

        Args:
            metadata (dict): Deezer JSON response for search query
            total (int): Number of record responses
            meta_csv_row (dict): Record for the CSV that is being generated
        """
        if not total:
            return

        meta_csv_row['artist'] = metadata['artist']['name']
        meta_csv_row['explicit'] = metadata['explicit_lyrics']

    def _parse_album_meta(self, metadata, meta_csv_row):
        """Internal parsing of Deezer Album metadata and record population

        Args:
            metadata (dict): Deezer JSON response for search query
            meta_csv_row (dict): Record for the CSV that is being generated
        """
        if 'error' in metadata.keys():  # if no record in api response simply return
            return

        try:  # Attempts to locate the genre name
            meta_csv_row['genre'] = metadata['genres']['data'][0]['name']
        except:
            pass

    def _empty_if_value(self, value, expected_empty):
        """Helper function to check if an API response is an alias to empty

        Args:
            value (any): Actual value
            expected_empty (any): Expect value of an empty response value.

        Returns:
            str|any: '' if any otherwise the value itself
        """
        return '' if value == expected_empty else value

    def create_empty_row(self):
        """Generates an empty CSV record.

        Returns:
            dict: [Empty dict with keys being all LABELS and values being ''
        """
        return {label: '' for label in LABELS}

    def get_url(self):
        """Getter for returning the the YT entity url that is being processed

        Returns:
            str: YT entity url
        """
        return self._url

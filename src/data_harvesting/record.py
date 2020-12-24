from clients.yt_media_fetcher.yt_media import YTMedia
from clients.metadata_scrapper.deezer_scrapper import DeezerScrapper

LABELS = ['file_name', 'artist', 'explicit', 'genre']


class Record:

    META_SEARCH_FIELDS_NUM = 3
    META_ALBUM_FIELDS_NUM = 1

    def __init__(self, url):

        self._yt_media = YTMedia()
        self._deezer_scrapper = DeezerScrapper()
        self._url = url

    def get_meta_row(self):

        title = self._yt_media.download_entity(self._url).strip()

        search_metadata = self._deezer_scrapper.search(title)
        meta_csv_row = self.creat_empty_row()
        meta_csv_row['file_name'] = title

        total = search_metadata['total']

        if not total:
            return meta_csv_row

        # naively choose first result
        search_metadata = search_metadata['data'][0]
        record_id = search_metadata['id']

        album_metadata = self._deezer_scrapper.album(record_id)

        self._parse_search_meta(search_metadata, total, meta_csv_row)
        self._parse_album_meta(album_metadata, meta_csv_row)

        return meta_csv_row

    def _parse_search_meta(self, metadata, total, meta_csv_row):

        if not total:
            return

        meta_csv_row['artist'] = metadata['artist']['name']
        meta_csv_row['explicit'] = metadata['explicit_lyrics']

    def _parse_album_meta(self, metadata, meta_csv_row):

        if 'error' in metadata.keys():
            return

        try:
            meta_csv_row['genre'] = metadata['genres']['data'][0]['name']
        except:
            pass

    def _empty_if_value(self, value, expected_empty):
        return '' if value == expected_empty else value

    def creat_empty_row(self):
        return {label: '' for label in LABELS}

    def get_url(self):
        return self._url

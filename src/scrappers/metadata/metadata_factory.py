from scrappers.base.base_factory import BaseFactory
from scrappers.metadata.api.deezer_metadata_scrapper import DeezerMetadataScrapper

class MetadataFactory(BaseFactory):

    def __init__(self):
        super().__init__()

        self._options['deezer'] = DeezerMetadataScrapper
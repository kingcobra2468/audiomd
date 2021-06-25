from scrappers.base.base_factory import BaseFactory
from scrappers.metadata.api.deezer_metadata_scrapper import DeezerMetadataScrapper

class MetadataFactory(BaseFactory):
    """Factory for generating metadata scrappers.
    """
    def __init__(self):
        super().__init__()

        self._options['deezer'] = DeezerMetadataScrapper
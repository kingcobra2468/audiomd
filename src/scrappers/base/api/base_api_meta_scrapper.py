from abc import ABC, abstractmethod

class BaseAPIMetaScrapper(ABC):

    LABELS=[]
    
    def __init__(self, labels):

        if not isinstance(labels, list):
            raise ValueError('labels must be of type list.')
        self.LABELS = labels

    def create_empty_row(self):
        """Generates an empty CSV record.

        Returns:
            dict: [Empty dict with keys being all LABELS and values being ''
        """
        return {label: '' for label in self.LABELS}

    @abstractmethod
    def get_meta_row(self):
        """Generates a metadata csv record for YT entity

        Returns:
            dict: Labeled CSV record
        """
        pass
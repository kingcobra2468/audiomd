from abc import ABC, abstractmethod


class BaseAPIMetaScrapper(ABC):
    """Base class for developing API/library driven metadata scrappers.
    """

    # the labels for the metadata for the metadata scrapper.
    LABELS=[]
    
    def __init__(self, labels):
        """Constructor.

        Args:
            labels (list(str)): The list of labels/features that the metadata scrapper
            will generate.

        Raises:
            ValueError: Thrown if labels are not of type list.
        """
        if not isinstance(labels, list):
            raise ValueError('labels must be of type list.')
        self.LABELS = labels

    def create_empty_row(self):
        """Generates an empty CSV record.

        Returns:
            dict: Empty dict with keys being all LABELS and values being ''.
        """
        return {label: '' for label in self.LABELS}

    @abstractmethod
    def get_meta_row(self):
        """Generates a metadata csv record for YT entity.

        Returns:
            dict: Labeled CSV record.
        """
        pass

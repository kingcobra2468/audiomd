from abc import ABC

class BaseFactory(ABC):

    def __init__(self):
        
        self._options = {}

    def create(self, option, *args, **kwargs):

        if option not in self._options:
            raise ValueError(f'Not valid factory option "{option}". Make sure option "{option}" ' +
                'is a valid content/metadata scrapper')

        return self._options[option](*args, **kwargs)

    @classmethod
    def new_instance(cls, option, *args, **kwargs):
        return cls().create(option, *args, **kwargs)
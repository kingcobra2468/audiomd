from abc import ABC

class BaseFactory(ABC):
    """Base factory from which other factories could be used to follow the
    factory pattern.
    """
    def __init__(self):
        
        self._options = {}

    def create(self, option, *args, **kwargs):
        """Creates an object from the available class definitions for the factory.

        Args:
            option (str): The key for the object to be generated.

        Raises:
            ValueError: Thrown when the option is not found in the list
            of classes in the factory.

        Returns:
            any: The object generated from the factory.
        """
        if option not in self._options:
            raise ValueError(f'Not valid factory option "{option}". Make sure option "{option}" ' +
                'is a valid content/metadata scrapper')

        return self._options[option](*args, **kwargs)

    @classmethod
    def new_instance(cls, option, *args, **kwargs):
        """Creates an object from the available class definitions for the factory.

        Args:
            option (str): The key for the object to be generated.

        Returns:
            any: The object generated from the factory.
        """
        return cls().create(option, *args, **kwargs)
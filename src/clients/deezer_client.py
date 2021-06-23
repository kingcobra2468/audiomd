from config import RAPIDAPI_KEY
import requests


class DeezerClient:
    """Scrapper wrapper for the Deezer API
    """
    # Paths for corresponding api's for various Deezer services
    SEARCH_API = 'https://deezerdevs-deezer.p.rapidapi.com/search'
    GENRE_API = 'https://deezerdevs-deezer.p.rapidapi.com/genre/'
    ALBUM_API = 'https://deezerdevs-deezer.p.rapidapi.com/album/'

    # TODO: update comment
    def __init__(self, rapidapi_key=RAPIDAPI_KEY):

        self._headers = {
            'x-rapidapi-key': rapidapi_key,
            'x-rapidapi-host': 'deezerdevs-deezer.p.rapidapi.com',
        }

    def search(self, text):
        """Peforms a metadata search query for a given song title

        Args:
            text (str): Name of the song.

        Returns:
            dict: Api JSON response
        """
        response = requests.request("GET", self.SEARCH_API, headers=self._headers, params={
            'q': text
        })

        return response.json()

    def genre(self, id):
        """Peforms a genre search query for a given Deezer record id

        Args:
            id (int): ID for a unique record from Deezer. Extracted from search query. 

        Returns:
            dict: Api JSON response
        """
        response = requests.request(
            "GET", f'{self.GENRE_API}{id}', headers=self._headers)

        return response.json()

    def album(self, id):
        """Peforms a album search query for a given Deezer record id

        Args:
            id (int): ID for a unique record from Deezer. Extracted from search query.

        Returns:
            dict: Api JSON response
        """
        response = requests.request(
            "GET", f'{self.ALBUM_API}{id}', headers=self._headers)

        return response.json()

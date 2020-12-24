from config import RAPIDAPI_KEY
import requests


class DeezerScrapper:

    SEARCH_API = 'https://deezerdevs-deezer.p.rapidapi.com/search'
    GENRE_API = 'https://deezerdevs-deezer.p.rapidapi.com/genre/'
    ALBUM_API = 'https://deezerdevs-deezer.p.rapidapi.com/album/'

    def __init__(self):

        self._headers = {
            'x-rapidapi-key': RAPIDAPI_KEY,
            'x-rapidapi-host': 'deezerdevs-deezer.p.rapidapi.com',
        }

    def search(self, text):

        response = requests.request("GET", self.SEARCH_API, headers=self._headers, params={
            'q': text
        })

        return response.json()

    def genre(self, id):

        response = requests.request(
            "GET", f'{self.GENRE_API}{id}', headers=self._headers)
        return response.json()

    def album(self, id):

        response = requests.request(
            "GET", f'{self.ALBUM_API}{id}', headers=self._headers)
        return response.json()

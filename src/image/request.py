import os


class UnsplashRequester:
    def __init__(self):
        self._base_url = 'https://api.unsplash.com'
        self._id = os.environ['UNSPLASH_CLIENT_ID']

    def search(self):
        pass

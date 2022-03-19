import os
from src.utils import send_request


class UnsplashRequester:
    def __init__(self):
        self._base_url = 'https://api.unsplash.com'

    @staticmethod
    def _get_auth_header():
        return {'Authorization': f'Client-ID {os.environ["UNSPLASH_CLIENT_ID"]}'}

    def search_photos(self, query: str, page: int = 1, per_page: int = 10):
        url = os.path.join(self._base_url, 'search', 'photos')
        headers = self._get_auth_header()
        params = {
            'query': query,
            'page': page,
            'per_page': per_page,
        }
        return send_request(url, "GET", headers=headers, params=params)

import os
import requests
from enum import (
    Enum,
    auto,
)

from src.utils import (
    send_request,
    pop_required_args,
    make_sure_dirs_exist,
)


class SearchMethod(Enum):
    RANDOM = auto()
    QUERY = auto()


class SearchQuality(Enum):
    RAW = "raw"
    FULL = "full"
    REGULAR = "regular"
    SMALL = "small"
    THUMB = "thumb"


class UnsplashRequester:
    """Reference: https://unsplash.com/documentation#get-a-random-photo"""

    def __init__(self):
        self._base_url = 'https://api.unsplash.com'

    @staticmethod
    def _get_auth_header():
        return {'Authorization': f'Client-ID {os.environ["UNSPLASH_CLIENT_ID"]}'}

    def _search_photos_by_query(self, query: str, page: int = 1, per_page: int = 30):
        url = os.path.join(self._base_url, 'search', 'photos')
        headers = self._get_auth_header()
        params = {
            'query': query,
            'page': page,
            'per_page': per_page,
        }
        return send_request(url, "GET", headers=headers, params=params)

    def _search_photos_by_random(self, query: str = None, count: int = 30):
        url = os.path.join(self._base_url, 'photos', 'random')
        headers = self._get_auth_header()
        params = {
            'query': query,
            'count': count,
        }
        return send_request(url, "GET", headers=headers, params=params)

    def search_photos(self, method: SearchMethod, **kwargs):
        if method is SearchMethod.QUERY:
            _args = pop_required_args(["query"], kwargs)
            res = self._search_photos_by_query(*_args, **kwargs)
        elif method is SearchMethod.RANDOM:
            res = self._search_photos_by_random(**kwargs)
        else:
            raise ValueError(f"searching method [{SearchMethod.value}] is unknown")
        return res

    def download_images_by_query(self,
                                 query: str,
                                 method: SearchMethod = SearchMethod.RANDOM,
                                 quality: SearchQuality = SearchQuality.REGULAR,
                                 save_dir: str = './photos',
                                 **kwargs
                                 ):
        photos_info = self.search_photos(method, query=query, **kwargs)
        save_dir = os.path.join(save_dir, query)
        make_sure_dirs_exist([save_dir])
        for info in photos_info:
            save_path = os.path.join(save_dir, f"{info['id']}.jpg")
            with open(save_path, "wb") as file:
                content = requests.get(info['urls'][quality.value]).content
                file.write(content)

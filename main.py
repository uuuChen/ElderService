from src.utils import load_os_environ
from src.notification import LineNotification
from src.image import UnsplashRequester


def main():
    load_os_environ()

    n = LineNotification()
    n.send_notify(image_file=open('./test/test.jpg', 'rb'), sticker_package_id=789, sticker_id=10855)

    r = UnsplashRequester()
    r.search_photos("mountain", per_page=1)


if __name__ == '__main__':
    main()

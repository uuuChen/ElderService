from src.utils import load_os_environ
from src.notification import LineNotification
from src.image import (
    SearchMethod,
    UnsplashRequester,
    SearchQuality,
)


def main():
    load_os_environ()

    n = LineNotification()
    n.send_notify(image_file=open('./test/test.jpg', 'rb'), sticker_package_id=789, sticker_id=10855)

    r = UnsplashRequester()
    r.download_images_by_query('cute', method=SearchMethod.RANDOM, quality=SearchQuality.REGULAR)


if __name__ == '__main__':
    main()

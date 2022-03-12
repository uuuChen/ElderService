from src.utils import load_os_environ
from src.notification import LineNotification


def main():
    load_os_environ()
    n = LineNotification()
    n.send_notify(image_file=open('./test/test.jpg', 'rb'), sticker_package_id=789, sticker_id=10855)


if __name__ == '__main__':
    main()

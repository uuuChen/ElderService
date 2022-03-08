
import os


class lineNotification:
    def __init__(self):
            self.base_url = "https://notify-api.line.me/api/notify"
            print(os.environ['LINE_NOTIFY_TOKEN'])
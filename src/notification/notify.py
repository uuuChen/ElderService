import os
import requests
from typing import (
    BinaryIO,
)
from ..utils import utils


class LineNotification:
    def __init__(self):
            self._base_url = "https://notify-api.line.me/api"
            self._authorization = f"Bearer {os.environ['LINE_NOTIFY_TOKEN']}"

    def send_notify(self,
                    message: str = " ",
                    image_thumb_nail: str = None,
                    image_full_size: str = None,
                    image_file: BinaryIO = None,
                    sticker_package_id: int = None,
                    sticker_id: int = None,
                    notification_disabled: bool = None,
                    ) -> int:
        # Check the arguments
        def _check_paired(val1: any, val2: any) -> bool:
            return utils.are_all_vals_None([val1, val2]) or utils.are_all_vals_not_None([val1, val2])

        if not _check_paired(image_thumb_nail, image_full_size):
            raise ValueError("Param [imageThumbnail] and [imageFullsize] need to be paired")
        if not _check_paired(sticker_package_id, sticker_id):
            raise ValueError("Param [stickerPackageId] and [stickerId] need to be paired")

        # Send the notify request
        notify_url = os.path.join(self._base_url, "notify")
        headers = {"Authorization": self._authorization}
        payload = { 
            "message":               message, 
            "imageThumbnail":        image_thumb_nail,
            "imageFullsize":         image_full_size,
            "notificationDisabled":  notification_disabled,
            "stickerPackageId":      sticker_package_id,
            "stickerId":             sticker_id,
        }
        files = {"imageFile": image_file}
        r = requests.post(notify_url, headers=headers, params=payload, files=files)

        return r.status_code

from __future__ import unicode_literals

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, 
    TextMessage, 
    ImageSendMessage,
)

from src.image import (
    UnsplashRequester,
    SearchMethod,
)

from src.config import (
    get_config,
    CONFIG_SECTION_LINE_BOT,
)

app = Flask(__name__)

line_bot_api = LineBotApi(get_config(CONFIG_SECTION_LINE_BOT, 'CHANNEL_ACCESS_TOKEN'))
line_bot_handler = WebhookHandler(get_config(CONFIG_SECTION_LINE_BOT, 'CHANNEL_SECRET'))


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        line_bot_handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@line_bot_handler.add(MessageEvent, message=TextMessage)
def handle_request(event):
    r = UnsplashRequester()
    photos_infos = r.search_photos(
        SearchMethod.RANDOM, 
        query=event.message.text,
        count=10,
    )

    most_likes_photo_info = max(photos_infos, key=lambda info: info['likes'])

    line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url=most_likes_photo_info['urls']['raw'],
            preview_image_url=most_likes_photo_info['urls']['thumb'],
        )
    )
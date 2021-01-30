from flask import Flask, request, abort
import logging
import os
import sys

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


app = Flask(__name__)


# ログを標準出力に出力する
app.logger.addHandler(logging.StreamHandler(sys.stdout))
# レベルの変更
app.logger.setLevel(logging.INFO)

#環境変数取得
CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "ヘルプ" or event.message.text == "help":
        reply_msg = "メニュー:\n"
        + "(なし) => オウム返し\n"
        + "カウント or count => 二行目からの文字数を数えます\n"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_msg))
    elif event.message.text.startswith("カウント\n"):
        txt = event.message.text.replace(" ","").replace("　","").replace("\n","").lstrip("カウント")
        reply_msg = "文字数は " + str(len(txt)) + "です。"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_msg))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
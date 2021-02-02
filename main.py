from flask import Flask, request, abort
import psycopg2
import os
from datetime import datetime, timedelta
import traceback

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from reminder.app import app
from reminder.models.models import Schedule


#環境変数取得
CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]
# DB_HOST = os.environ["DB_HOST"]
# DB_PORT = os.environ["DB_PORT"]
# DB_DBNAME = os.environ["DB_DBNAME"]
# DB_USER = os.environ["DB_USER"]
# DB_PASSWORD = os.environ["DB_PASSWORD"]

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
    msg_from = event.message.text
    if msg_from == "ヘルプ" or msg_from == "help":
        # ヘルプメニュー
        reply_msg = "メニュー:\n" \
        + "(なし) => オウム返し\n" \
        + "カウント or count => 二行目からの文字数を数えます(改行、空白は除きます)"
        # + "日付 => 今日の日付を返します\n" \
    elif msg_from.startswith("カウント\n") or msg_from.startswith("count\n"):
        # メッセージの文字数カウント
        txt = msg_from.replace(" ","").replace("　","").replace("\n","").lstrip("カウント").lstrip("count")
        reply_msg = "文字数は " + str(len(txt)) + " 文字です。"
    elif msg_from.startswith("登録\n"):
        # 登録
        # 時間: %Y/%m/%d %H:%M
        # メッセージ
        try:
            profile = line_bot_api.get_profile(event.source.user_id)
            app.logger.info(f"user profile => {profile}")
            data = msg_from.split("\n")
            message = data[2]
            time = datetime.strptime(data[1], '%Y/%m/%d %H:%M')
            result = Schedule.create(profile.user_id, profile.display_name, message, time)
            app.logger.info(f"create => {result}")

            reply_msg = "リマインドを登録しました。"
        except:
            app.logger.warning(traceback.format_exc())
            reply_msg = "リマインドの登録に失敗しました。"
    else:
        # それ以外はオウム返し
        reply_msg = msg_from
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_msg))

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
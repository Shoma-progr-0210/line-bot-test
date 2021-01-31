from flask import Flask, request, abort
import psycopg2
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
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_DBNAME = os.environ["DB_DBNAME"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# DBコネクション取得関数
def get_connection():
    dsn = "host=" + DB_HOST \
        + "port=" + str(DB_PORT) \
        + "dbname=" + DB_DBNAME \
        + "user=" + DB_USER \
        + "password=" + DB_PASSWORD
    
    return psycopg2.connect(dsn)

def get_response_message(msg_from):
    if msg_from=="日付":
        # "日付"が入力された時だけDBアクセス
        with get_connection() as conn:
            with conn.cursor(name="cs") as cur:
                try:
                    sql_str = "SELECT TO_CHAR(CURRENT_DATE, 'yyyy/mm/dd');"
                    cur.execute(sql_str)
                    (reply_msg,) = cur.fetchone()
                    return reply_msg
                except:
                    reply_msg = "exception"
                    return reply_msg
    elif msg_from == "ヘルプ" or msg_from == "help":
        # ヘルプメニュー
        reply_msg = "メニュー:\n" \
        + "(なし) => オウム返し\n" \
        + "日付 => 今日の日付を返します\n" \
        + "カウント or count => 二行目からの文字数を数えます(改行、空白は除きます)"
        return reply_msg
    elif msg_from.startswith("カウント\n") or msg_from.startswith("count\n"):
        # メッセージの文字数カウント
        txt = msg_from.replace(" ","").replace("　","").replace("\n","").lstrip("カウント").lstrip("count")
        reply_msg = "文字数は " + str(len(txt)) + " 文字です。"
        return reply_msg
    else:
        # それ以外はオウム返し
        reply_msg = msg_from
        return reply_msg

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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=get_response_message(event.message.text)))

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
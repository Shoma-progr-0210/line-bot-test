from flask import Flask
import os
import logging
import sys

from reminder.database import init_db
import reminder.models


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_db(app)


# ログを標準出力に出力する
app.logger.addHandler(logging.StreamHandler(sys.stdout))
# レベルの変更
app.logger.setLevel(logging.INFO)
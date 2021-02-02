from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import logging
import sys

from .models import models

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ログを標準出力に出力する
app.logger.addHandler(logging.StreamHandler(sys.stdout))
# レベルの変更
app.logger.setLevel(logging.INFO)
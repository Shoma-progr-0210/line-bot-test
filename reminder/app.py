from flask import Flask
import os
import logging

from reminder.database import init_db
import reminder.models


app = Flask(__name__)

# レベルの変更
app.logger.setLevel(logging.INFO)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# with app.app_context():
init_db(app)
db.app = app
# リマインドスケジュール起動
from reminder.remind import scheduler_start
scheduler_start(app)

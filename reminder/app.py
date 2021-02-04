from flask import Flask
import os
import logging

from reminder.database import init_db
import reminder.models
from reminder.jobs import job


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_db(app)

# レベルの変更
app.logger.setLevel(logging.INFO)
# jobの追加
app.cli.add_command(job)
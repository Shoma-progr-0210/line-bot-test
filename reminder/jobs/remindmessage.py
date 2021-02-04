from datetime import datetime, timedelta
import os

from linebot import LineBotApi
from linebot.models import TextSendMessage

from flask import current_app, logging
from reminder.models.schedule import Schedule, ScheduleSchema
from reminder.service.messageservice import MessageService


logger = logging.create_logger(current_app)
# 環境変数取得
CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def remind_message():
    time_now = datetime.now().replace(microsecond=0).replace(second=0) + timedelta(hours=9)
    logger.info(f"reminds start. time now => {time_now}")
    remind_schedules = Schedule.get_by_time(time_now)
    schedule_schema = ScheduleSchema(many=True)
    message_service = MessageService()
    remind_msgs = message_service.create_reminds_from_list(schedule_schema.dump(remind_schedules))

    for user_id, msg in remind_msgs.items():
        messages = TextSendMessage(text=msg)
        line_bot_api.push_message(user_id, messages=messages)

    logger.info(f"reminds done. total count => {len(remind_msgs.keys())}")
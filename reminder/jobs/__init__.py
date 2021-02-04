from flask.cli import AppGroup
from reminder.jobs.remindmessage import remind_message

# グループを作成
job = AppGroup('job')

# task関連のコマンドを追加していく
job.add_command(remind_message)
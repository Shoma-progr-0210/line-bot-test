from flask_apscheduler import APScheduler
from reminder.jobs.remindmessage import remind_message


class Config(object):
    SCHEDULER_API_ENABLED = True
    JOBS = [
        {
            'id': 'remind_job',
            'func': 'remind_job',
            'trigger': 'interval',
            'seconds': 60
        }
    ]

scheduler = APScheduler()

def remind_job():
    print('This job is run every a minute.')
    remind_message()


def scheduler_start(app):
    app.config.from_object(Config())
    scheduler.init_app(app)
    # scheduler.api_enabled = True
    scheduler.start()
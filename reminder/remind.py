from flask_apscheduler import APScheduler
from reminder.jobs.remindmessage import remind_message


class Config(object):
    SCHEDULER_API_ENABLED = True
    # JOBS = [
    #     {
    #         'id': 'remind_job',
    #         'func': 'remind_job',
    #         'trigger': 'interval',
    #         'minutes': 1
    #     }
    # ]

scheduler = APScheduler()

def remind_job():
    print('This job is run every a minute.')
    remind_message()


def scheduler_start(app):
    scheduler.init_app(app)
    # app.config.from_object(Config())
    scheduler.api_enabled = True
    scheduler.add_job('remind_job', remind_job, 'interval', minutes=1)
    scheduler.start()
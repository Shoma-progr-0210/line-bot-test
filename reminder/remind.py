from flask_apscheduler import APScheduler
from reminder.jobs.remindmessage import remind_message


class Config(object):
    SCHEDULER_API_ENABLED = True

scheduler = APScheduler()

# リマインド
@scheduler.task('cron', id='remind_job', minute='*')
def remind_job():
    app = scheduler.app
    with app.app_context():
        app.logger.info('This job is run every a minute.')
        remind_message()


def scheduler_start(app):
    app.config.from_object(Config())
    # scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()
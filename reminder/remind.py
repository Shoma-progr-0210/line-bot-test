from apscheduler.schedulers.blocking import BlockingScheduler
from reminder.jobs.remindmessage import remind_message


def remind_job():
    print('This job is run every a minute.')
    remind_message()


def sched_start():
    sched = BlockingScheduler(daemon=True)
    sched.add_job(remind_job, 'interval', minute=1)
    sched.start()
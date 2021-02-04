from apscheduler.schedulers.blocking import BlockingScheduler
from reminder.jobs.remindmessage import remind_message

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def remind_job():
    print('This job is run every a minute.')
    remind_message()


def sched_start():
    sched.start()
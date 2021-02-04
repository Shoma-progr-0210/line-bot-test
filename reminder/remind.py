from apscheduler.schedulers.blocking import BlockingScheduler
from reminder.jobs.remindmessage import remind_message


sched = BlockingScheduler(daemon=True)

def remind_job():
    print('This job is run every a minute.')
    # remind_message()


def sched_start():
    sched.add_job(remind_job, 'interval', minutes=1)
    sched.start()
from . import LOGS
import datetime, logging

#def gunluk(context):





def gunluk():
    zaman = datetime.datetime.now()
    print('Günlük Saniye: ',zaman.second)
    

def eliif():
    zaman = datetime.datetime.now()
    if zaman.hour == 17:
        from random import choice
        emoji = choice(['💖','🦄','🌻','❤️','🦥','🦦','🍀','💃🏻'])
        hitap = choice(['👉🏻👈🏻','lna','hatırlatıyım'])





'''*************************************'''

LOGUKAPAT = logging.getLogger('apscheduler.executors.default')
LOGUKAPAT.setLevel(logging.ERROR)

'''*************************************'''



"""
    while True:
        zaman = datetime.datetime.now()
        if zaman.second in [30,32]:
            bot.send_message(berce, 'Başarılı!', disable_notification=True)
        sleep(2)

"""
#updater.job_queue.run_daily(gunluk, time=datetime.datetime.strptime("15:25:00", '%H:%M:%S').time(), name="test")
#updater.job_queue.run_once(gunluk, 10, name="test")

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_executor('processpool')
scheduler.add_job(gunluk,  'interval', seconds=10)
scheduler.start()


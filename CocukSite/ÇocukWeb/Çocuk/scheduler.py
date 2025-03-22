from apscheduler.schedulers.background import BackgroundScheduler
from .utils import *

def start():
    scheduler = BackgroundScheduler()
    # Her 6 saatte bir güncelle (API limitlerini aşmamak için)
    scheduler.add_job(aktivite_guncelle, 'interval', hours=6)
    scheduler.add_job(bilmece_guncelle, 'interval', hours=6)
    scheduler.add_job(doga_bilgisi_guncelle, 'interval', hours=6)
    scheduler.add_job(yemek_tarifi_guncelle, 'interval', hours=6)
    scheduler.add_job(hikaye_guncelle, 'interval', hours=6)
    scheduler.add_job(el_sanatlari_guncelle, 'interval', hours=6)
    scheduler.start()
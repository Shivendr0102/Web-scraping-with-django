from apscheduler.schedulers.background import BackgroundScheduler
from blog import views
from rest_framework.views import APIView
from datetime import datetime
# from urllib import request

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(views.scrape, 'interval' , minutes = 1)
    scheduler.start()

# ApScheduler Imports
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

# Native Imports
import sys
import random

# Django Imports
from django.contrib.auth import get_user_model
from django.conf import settings

# SOTP Helpers Imports
from sotp.helpers.remove_otps import remove_user_otp


User = get_user_model()


def run_scheduler(user_email:str):
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    
    # run remove user totps and otps job every 15 minutes
    scheduler.add_job(
        remove_user_otp, 
        'interval', minutes=settings.SOTP_TIME_EXPIRATION,
        jobstore='default',
        id="{}-{}_remove_elapsed_otps".format(user_email, random.randint(00000000, 9000000)),
    )

    # Start scheduler
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)
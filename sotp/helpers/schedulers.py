# ApScheduler Imports
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

# Native Imports
import sys

# Django Imports
from django.contrib.auth import get_user_model

# SOTP Helpers Imports
from sotp.helpers.remove_otps import remove_user_sotps


User = get_user_model()


def run_scheduler(user:User):
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    
    # run remove user totps and otps job every 15 minutes
    scheduler.add_job(
        remove_user_sotps, 
        'interval', minutes=15,
        jobstore='default',
        id="#{}_totp_{}_otp_{}".format(user.id, user.totp, user.otp),
    )

    # Start scheduler
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)
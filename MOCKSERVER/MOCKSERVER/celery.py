from __future__ import absolute_import
import os
from django.conf import settings
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','MOCKSERVER.settings')#it saves your from always passing in the settings modules to the celery program. It Must always come before creating the app Instances,Which is what We do next:

#Celery configuration
app = Celery('MOCKSERVER')
app.config_from_object('django.conf:settings')# using a string is better since then the worker doesn't have to serialize the object when using other os systems.like windows or execv:
app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)#autodiscover all installed apps define all tasks in a separate tasks.py module ,in this define format ,


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
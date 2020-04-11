from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
# replace app.settings with your django settings.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ecommerce.settings')
app = Celery('Ecommerce',
                  broker='pyamqp://guest@localhost//',
include=['Ecommerce.tasks'])
if __name__ == '__main__':
        print("executed")
        app.start()
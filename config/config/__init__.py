from __future__ import absolute_import, unicode_literals

from .celery import app as celery_app

__all__ = ('celery_app',)                   # Это позволит убедиться, что приложение всегда импортируется, когда запускается Django
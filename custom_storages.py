from django.conf import settings
from storages.backends.s3boto3 import s3boto3Storage


class StaticStorage(s3boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(s3boto3Storage):
    location = settings.MEIDAFILES_LOCATION

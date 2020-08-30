from django.db import models


class Mapper(models.Model):
    hashcode = models.CharField(max_length=10, unique=True)
    url = models.TextField(unique=True)
    clicks = models.IntegerField(default=0)
    url_shorten_count = models.IntegerField(default=1)
    creation_timestamp = models.DateTimeField(auto_now_add=True)

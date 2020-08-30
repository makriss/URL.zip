from django.db import models


class UrlMapper(models.Model):
    hashcode = models.CharField(max_length=15, unique=True)
    url = models.TextField(unique=True)
    clicks = models.IntegerField(default=0)
    url_shorten_count = models.IntegerField(default=1)
    creation_timestamp = models.DateTimeField(auto_now_add=True)

    @classmethod
    def save_hashcode(cls, hashcode, url):
        return cls.objects.create(hashcode=hashcode, url=url)

    def increment_url_shorten_count(self):
        self.url_shorten_count = 1 + self.url_shorten_count
        self.save()
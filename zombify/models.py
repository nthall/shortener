from django.db import models

class Zomburl(models.Model):
    zomblink = models.CharField(max_length=16)
    destination_url = models.CharField(max_length=200)
    added = models.DateTimeField('timestamp of url creation')
    last_accessed = models.DateTimeField('timestamp of last access')
    hits = models.IntegerField()

    def __unicode__(self):
        return self.zomblink + ' redirects to ' + self.destination_url


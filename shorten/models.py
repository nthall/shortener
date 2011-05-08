from django.db import models

class UrlPair(models.Model):
    code = models.CharField(max_length=16)
    destination_url = models.CharField(max_length=200)
    added = models.DateTimeField('timestamp of url creation')
    last_accessed = models.DateTimeField('timestamp of last access', blank=True, null=True)
    hits = models.IntegerField(blank=True,null=True)

    def __unicode__(self):
        return self.code + ' redirects to ' + self.destination_url


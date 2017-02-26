from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.

class Movie(models.Model):
    uploader = models.ForeignKey("auth.User")
    title = models.CharField(max_length=200)
    desc = models.TextField()
    pic_url = models.TextField()
    m_type = models.IntegerField()
    quality = models.IntegerField()
    status = models.IntegerField()
    create_date = models.DateField(
        blank=True, null=True)
    publish_date = models.DateField(
        blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

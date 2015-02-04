#-*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import now

class Image(models.Model):
    upload_date = models.DateTimeField(default=now)
    file_name = models.CharField(max_length = 255)
    set_proc = models.CharField(max_length=255,blank=True, default='DEFAULT_PROC')
    set_tag = models.CharField(max_length=255,blank=True,default='DEFAULT_TAG')
    set_threshold = models.CharField(max_length=255,blank=True,default='DEFAULT_THRESHOLD')
#    upload_date = models.DateTimeField('date upload')
    def __unicode__(self):
        return self.file_name

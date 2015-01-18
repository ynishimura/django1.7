#-*- coding: utf-8 -*-
from django.db import models

class Image(models.Model):
    file_name = models.CharField(max_length = 255)
    set_proc = models.CharField(max_length=255,blank=True, default='DEFAULT_PROC')
    set_tag = models.CharField(max_length=255,blank=True,default='DEFAULT_TAG')
#    upload_date = models.DateTimeField('date upload')
    def __unicode__(self):
        return self.file_name

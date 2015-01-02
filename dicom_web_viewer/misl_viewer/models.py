from django.db import models

class Upload(models.Model):
    file_name = models.CharField(max_length = 255)
    upload_date = models.DateTimeField('date upload')
    def __unicode__(self):
        return self.name

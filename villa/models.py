from django.db import models

# Create your models here.


class Villa(models.Model):
    title = models.CharField(max_length=180, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    short_desc = models.CharField(verbose_name='Details', max_length=500, blank=True, null=True)
    desc = models.TextField(verbose_name='Description', blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

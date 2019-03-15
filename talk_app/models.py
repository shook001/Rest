from django.db import models


class Talk(models.Model):
    ID = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    speaker = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.name

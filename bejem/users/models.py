from django.db import models

class User(models.Model):
    login = models.CharField('login', max_length=64)
    email = models.EmailField('email', blank=True)

    def __unicode__(self):
        return "%s %s" % (self.login, self.email)

    class Meta:
        ordering = ["login"]

    #class Admin:
    #    pass

from django.db import models

class User(models.Model):
    login = models.CharField('login', max_length=64)
    email = models.EmailField('email', blank=True)

    def __str__(self):
        return '%s' % (self.login)

    #class Admin:
    # pass
 
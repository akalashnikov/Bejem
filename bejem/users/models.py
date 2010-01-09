from django.db import models
from django.contrib.auth.models import User, UserManager
from dics.models import City


class Member(User):
    SEX_CHOISES = (('M', 'Male'),('F', 'Female'),)
    #user = models.ForeignKey(User) This field is inherited from  models.User
    #fullname = models.CharField(max_length=128) models.User has first and last name
    sex = models.CharField(max_length=1, choices=SEX_CHOISES)
    city = models.ForeignKey(City, null=True)

    objects = UserManager()

    class Meta:
        ordering = ["username"]

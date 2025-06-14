# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    front_desk_1 = models.TextField(max_length=255, null=True, blank=True)
    front_desk_2 = models.TextField(max_length=255, null=True, blank=True)
    manager = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Bed(models.Model):

    #__Bed_FIELDS__
    bed_1 = models.CharField(max_length=255, null=True, blank=True)
    bed_2 = models.CharField(max_length=255, null=True, blank=True)

    #__Bed_FIELDS__END

    class Meta:
        verbose_name        = _("Bed")
        verbose_name_plural = _("Bed")


class Guest(models.Model):

    #__Guest_FIELDS__
    gest_1 = models.TextField(max_length=255, null=True, blank=True)
    gest_2 = models.TextField(max_length=255, null=True, blank=True)

    #__Guest_FIELDS__END

    class Meta:
        verbose_name        = _("Guest")
        verbose_name_plural = _("Guest")


class Payment(models.Model):

    #__Payment_FIELDS__
    paid_1 = models.IntegerField(null=True, blank=True)
    paid_2 = models.IntegerField(null=True, blank=True)

    #__Payment_FIELDS__END

    class Meta:
        verbose_name        = _("Payment")
        verbose_name_plural = _("Payment")


class Room(models.Model):

    #__Room_FIELDS__
    room_1 = models.IntegerField(null=True, blank=True)
    room_2 = models.IntegerField(null=True, blank=True)

    #__Room_FIELDS__END

    class Meta:
        verbose_name        = _("Room")
        verbose_name_plural = _("Room")


class Meal(models.Model):

    #__Meal_FIELDS__
    meal_1 = models.CharField(max_length=255, null=True, blank=True)
    meal_2 = models.CharField(max_length=255, null=True, blank=True)

    #__Meal_FIELDS__END

    class Meta:
        verbose_name        = _("Meal")
        verbose_name_plural = _("Meal")



#__MODELS__END

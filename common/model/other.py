from django.db import models
from django.conf import settings


class PhoneCodes(models.Model):
    phone = models.PositiveIntegerField(default=0, verbose_name="Телефон")
    code = models.PositiveSmallIntegerField(default=0, verbose_name="Код")

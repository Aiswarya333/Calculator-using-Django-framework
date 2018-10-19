from django.db import models

class Calc(models.Model):
    num1 = models.CharField(max_length=30)
    num2 = models.CharField(max_length=30)
    
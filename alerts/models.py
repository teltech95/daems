from django.db import models

# Create your models here.


class SendReport(models.Model):
    user = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    lat = models.CharField(max_length=200)
    long = models.CharField(max_length=200)
    case = models.CharField(max_length=200)
    createdAt = models.CharField(max_length=200)
    report_title = models.CharField(max_length=200)
    # image =

    def __str__(self):
        return self.report_title


class EcoContribution(models.Model):
    user = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)

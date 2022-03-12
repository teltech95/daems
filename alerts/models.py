from django.db import models

# Create your models here.


class DisasterAlerts(models.Model):
    eathquake = 'eathquake'
    cyclone = 'cyclone'
    drought = 'dought'
    floods = 'floods'
    volcano = 'volcano'
    wildFires = 'wildFires'
    others = 'others'

    event_type_choices = [
        (eathquake, 'eathquake'),
        (cyclone, 'cyclone'),
        (drought, 'drought'),
        (floods, 'floods'),
        (volcano, 'volcano'),
        (wildFires, 'wildFires'),
        (others, 'others'),
    ]

    event_id = models.BigIntegerField(unique=True)
    location = models.CharField(max_length=100)
    event_title = models.CharField(max_length=100)
    magnitude = models.CharField(max_length=100)
    createAt = models.DateTimeField(auto_now_add=True)
    expected_date = models.DateField()
    description = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=100)  # (lat, long)
    event_type = models.CharField(
        max_length=100, choices=event_type_choices, default='others')
    link = models.CharField(max_length=100)
    population = models.BigIntegerField()  # population affected
    alert_level = models.IntegerField()
    country = models.CharField(max_length=100)
    latitude = models.FloatField(default='')
    longitude = models.FloatField(default='')

    def __str__(self):
        return self.event_type

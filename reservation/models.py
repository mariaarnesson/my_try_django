from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime


GUEST_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),   
    )

TABLE_CHOICES = (
    ("Family table", "Family table"),
    ("Outdoor seating", "Outdoor seating"),
    ("Table for two", "Table for two"),
    ("Table on second floor (sea view)", "Table on second floor (sea view)")
    )

TIME_CHOICES = (
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
    ("8 PM", "8 PM"),
    ("8:30 PM", "8:30 PM"),
    ("9 PM", "9 PM"),
    ("9:30 PM", "9:30 PM"),
    ("10 PM", "10 PM"),
    ("10:30 PM", "10:30 PM"),
)


class Reservation(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=70, blank=True, unique=True)
    date = models.DateField(default=datetime.now)
    no_of_guest = models.CharField(
        max_length=2, choices=GUEST_CHOICES, verbose_name="no of guest")
    table = models.CharField(max_length=50, choices=TABLE_CHOICES, default="Family table")
  

class TablesModel(models.Model):
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="6 PM")

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"

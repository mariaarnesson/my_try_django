from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


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


SERVICE_CHOICES = (
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


class Table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Family table")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="6 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    guest = models.CharField(
        max_length=2, choices=GUEST_CHOICES, verbose_name="guest")

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
 
    class Meta:
        verbose_name = "Table"
        verbose_name_plural = "Tables"

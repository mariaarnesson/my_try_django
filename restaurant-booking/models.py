from django.db import models
from django.utils.html import format_html
from account.models import User, IPAddress
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from extensions.utils import jalali_converter


# Create your models here.


class BookTable(models.Model):
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
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booked_tables", verbose_name="book table")
    date = models.DateTimeField(verbose_name="date")
    phone_number = models.DecimalField(
        max_digits=11, decimal_places=0, verbose_name="phone number")
    guest = models.CharField(
        max_length=2, choices=GUEST_CHOICES, verbose_name="guest")

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"

    class Meta:
        verbose_name = "Book Table"
        verbose_name_plural = "Book Tables"

    def get_absolute_url(self):
        return reverse("account:booked_tables")

    def jdate(self):
        return jalali_converter(self.date)
    jdate.short_description = "date"
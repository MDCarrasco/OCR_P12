from django.conf import settings
from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    mobile = models.CharField(max_length=20, blank=False)
    company_name = models.CharField(max_length=100, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Contract(models.Model):
    status = models.BooleanField(blank=False)
    amount = models.FloatField(blank=False)
    payment_due = models.DateTimeField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class Event(models.Model):
    status = models.BooleanField(blank=False)
    attendees = models.IntegerField(blank=False)
    event_date = models.DateTimeField(blank=False)
    notes = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

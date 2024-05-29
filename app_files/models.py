from django.db import models

from django.db.models.signals import post_save

from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser

import datetime
from datetime import datetime  
import pytz  





class User_Profile(AbstractUser):

    email = models.CharField(max_length=40, blank=True, null=True, unique=True)


class MasterInventory(models.Model):

    item_number = models.CharField(max_length=8, unique=True)

    total_quantity = models.IntegerField(default=0)

    ITEM_CLASS_CHOICES=(

        ('WP','Wp'),
        ('Other','Other'),
    )

    item_class= models.CharField(default='WP',max_length=8, choices=ITEM_CLASS_CHOICES)

    NON_MATERIAL=(

        ('N','n'),
        ('',''),
    )

    non_material= models.CharField(default='', max_length=2, choices=NON_MATERIAL)


    description = models.CharField(max_length=45)

    now=datetime.now(pytz.timezone('US/Central'))  


    date = models.DateTimeField(default=now)

    def __str__(self):

        return self.item_number


class InventoryTransaction(models.Model):

    item_number = models.ForeignKey(MasterInventory, on_delete=models.CASCADE)

    IN_OUT_CHOICES = (

        ('IN', 'In'),

        ('OUT', 'Out'),

    )

    IN_OUT = models.CharField(max_length=10, choices=IN_OUT_CHOICES, null=True, blank=True)

    transaction_quantity = models.IntegerField()

    date = models.DateTimeField(auto_now_add=True)

    start_quantity = models.IntegerField(blank=True, null=True)


    def save(self, *args, **kwargs):

        if not self.start_quantity:

            self.start_quantity = self.item_number.total_quantity

        super().save(*args, **kwargs)

    def __str__(self):

        return f"{self.item_number} - {self.IN_OUT}"

@receiver(post_save, sender=InventoryTransaction)

def update_total_quantity(sender, instance, **kwargs):

    if instance.transaction_quantity:

        instance.item_number.total_quantity += instance.transaction_quantity

    instance.item_number.save()
from django.db import models

from django.db.models.signals import post_save

from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser



class User_Profile(AbstractUser):

    email = models.CharField(max_length=40, blank=True, null=True, unique=True)



class MasterInventory(models.Model):

    item_number = models.CharField(max_length=8, unique=True)

    total_quantity = models.IntegerField(default=0)  # Default to 0

    description = models.CharField(max_length=45)



    def __str__(self):

        return self.item_number



class InventoryTransaction(models.Model):

    item_number = models.ForeignKey(MasterInventory, on_delete=models.CASCADE)

    IN_OUT = models.CharField(max_length=10, blank=True, null=True)

    transaction_quantity = models.IntegerField()

    
    def __str__(self):

        return f"{self.item_number} - {self.IN_OUT}"



# Signal to update total_quantity in MasterInventory

@receiver(post_save, sender=InventoryTransaction)

def update_total_quantity(sender, instance, **kwargs):

    if instance.transaction_quantity < 0:

        new_in_out = 'OUT'

        instance.item_number.total_quantity += instance.transaction_quantity

    elif instance.transaction_quantity > 0:

        new_in_out = 'IN'

        instance.item_number.total_quantity += instance.transaction_quantity


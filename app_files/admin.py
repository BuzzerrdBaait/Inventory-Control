
from django.contrib import admin

from .models import User_Profile, MasterInventory, InventoryTransaction

import random

from django.db import IntegrityError

@admin.register(User_Profile)

class UserProfilesAdmin(admin.ModelAdmin):

    list_display = ['username', 'email', 'last_login']


@admin.register(MasterInventory)

class MasterInventoryAdmin(admin.ModelAdmin):

    list_display = ['item_number', 'total_quantity', 'description', 'date','item_class','non_material']

    search_fields = ['item_number']

    def generate_test_data(self, request, queryset):

        for i in range(9):

            item_number = f"000-{i:03}"

            try:

                non_material='N' if random.random() < 0.60 else ''

                item = MasterInventory.objects.create(item_number=item_number, total_quantity=0, description="Blah blah blah", non_material=non_material)

            except IntegrityError:

                self.message_user(request, f"'{item_number}' already exists. Or there is a query error.")

                continue
        

            for t in range(100):

                if t < 1:
                    transaction_type= 'IN'
                    non_material='n'

                else:
                    transaction_type = 'OUT' if random.random() < 0.92 else 'IN'
                    

                if transaction_type == 'OUT':

                    transaction_quantity = random.randint(-4, -1)

                else:

                        transaction_quantity = random.randint(25, 40)


                transaction = InventoryTransaction.objects.create(item_number=item, IN_OUT=transaction_type, transaction_quantity=transaction_quantity)

                item.save()



        self.message_user(request, "Test data generated successfully.")

    actions = [generate_test_data]





@admin.register(InventoryTransaction)

class InventoryTransactionsAdmin(admin.ModelAdmin):

    list_display = ['item_number','start_quantity', 'IN_OUT','transaction_quantity', 'date']

    list_filter = ['IN_OUT', 'date']

    search_fields = ['item_number__item_number']



    def save_model(self, request, obj, form, change):

        if obj.transaction_quantity > 0:

            obj.IN_OUT = 'IN'

        elif obj.transaction_quantity < 0:

            obj.IN_OUT = 'OUT'

        super().save_model(request, obj, form, change)


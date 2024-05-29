import random

from django.test import TransactionTestCase

from .models import MasterInventory, InventoryTransaction



def create_master_inventory_items():

    """Function to create MasterInventory items"""

    item_descriptions = {

        'Item 1': 'Description 1',

        'Item 2': 'Description 2',

        'Item 3': 'Description 3'

    }

    for i in range(1000):

        item_number = f"{i:03d}-{i:03d}"

        description = random.choice(list(item_descriptions.keys()))

        MasterInventory.objects.create(item_number=item_number, total_quantity=0, description=description)



def perform_random_transactions():

    """Function to perform random transactions"""

    items = MasterInventory.objects.all()

    for _ in range(100):  # Perform 100 random transactions

        item = random.choice(items)

        IN_OUT = random.choice(['IN', 'OUT'])

        if IN_OUT == 'IN':

            transaction_quantity = random.randint(0, 100)

        else:

            transaction_quantity = random.randint(-20, -1)

        InventoryTransaction.objects.create(item_number=item, IN_OUT=IN_OUT, transaction_quantity=transaction_quantity)



class InventoryTestCase(TransactionTestCase):

    def test_inventory_creation(self):

        """Test MasterInventory creation"""

        create_master_inventory_items()

        self.assertEqual(MasterInventory.objects.count(), 1000)



    def test_random_transactions(self):

        """Test random transactions"""

        create_master_inventory_items()

        perform_random_transactions()

        self.assertEqual(InventoryTransaction.objects.count(), 100)


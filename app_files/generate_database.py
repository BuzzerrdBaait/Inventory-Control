import random
from models import MasterInventory,InventoryTransaction

def create_master_inventory_items():

    """Function to create MasterInventory items"""

    item_descriptions = {

        'Item 1': 'Description 1',

        'Item 2': 'Description 2',

        'Item 3': 'Description 3'

    }

    for i in range(6):

        item_number = f"{i:03d}-{i:03d}"

        description = random.choice(list(item_descriptions.keys()))

        MasterInventory.objects.create(item_number=item_number, total_quantity=0, description=description)



def perform_random_transactions():

    """Function to perform random transactions"""

    items = MasterInventory.objects.all()

    for _ in range(50):  # Perform 100 random transactions

        item = random.choice(items)

        IN_OUT = random.choice(['IN', 'OUT'])

        if IN_OUT == 'IN':

            transaction_quantity = random.randint(0, 50)

        else:

            transaction_quantity = random.randint(-10, -1)

        InventoryTransaction.objects.create(item_number=item, IN_OUT=IN_OUT, transaction_quantity=transaction_quantity)


make_database=create_master_inventory_items(),perform_random_transactions()


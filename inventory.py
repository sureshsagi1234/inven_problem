'''
Created on Jan 11, 2017

@author: sureshsagiraju
'''


'''
    Inventory allocator:
    There should be an inventory allocator which allocates inventory to the inbound data according to the following rules:
    1) Inbound orders to the allocator should be individually identifyable (ie two streams may generate orders with an identical header, but these orders should be identifyable from their streams)
    2) Inventory should be allocated on a first come, first served basis; once allocated, inventory is not available to any other order.
    3) Inventory should never drop below 0.
    4) If a line cannot be satisfied, it should not be allocated.  Rather, it should be  backordered (but other lines on the same order may still be satisfied).
    5) When all inventory is zero, the system should halt and produce output listing, in the order received by the system, the header of each order, the quantity on each line, the quantity allocated to each line, and the quantity backordered for each line.

'''


class Inventory(object):

    '''
        Constructor expects product inventory
        @parm store - a dict of product inventory
    '''

    def __init__(self, store):
        self.store = store

    '''
        returns the current inventory dict
    '''

    def get_inventory(self):
        return self.store

    '''
        returns True if inventory is empty
    '''

    def check_inventory_is_emptry(self):
        total_product_count = 0
        for val in self.store:
            total_product_count += self.store[val]
        if total_product_count == 0:
            return True
        else:
            return False

    '''
        checks if the requested products are available and returns allocated and backordered count
    '''

    def allocate(self, product, count):
        if self.store[product] >= count:
            self.store[product] -= count
            return 0, count
        else:
            return count, 0


if __name__ == "__main__":
    # quick tests
    store = {}
    store['A'] = 5
    store['B'] = 5
    store['C'] = 5
    store['D'] = 5
    store['E'] = 5
    inv = Inventory(store)
    print inv.check_inventory_is_emptry()

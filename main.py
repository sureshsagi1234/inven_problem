'''
Created on Jan 11, 2017

@author: sureshsagiraju
'''
# will set streams etc for orders

# call allocator with inventory

from data_source import DataSource
from inventory import Inventory
from validator import Validator
from allocator import Allocator


if __name__ == "__main__":

    store = {}
    store['A'] = 250
    store['B'] = 250
    store['C'] = 250
    store['D'] = 250
    store['E'] = 250

    min_demand = 1
    max_demand = 5
    number_of_streams = 3
    number_of_orders = 10

    validator = Validator(store.keys(), min_demand, max_demand)
    data_source = DataSource(
        number_of_streams, store.keys(), min_demand, max_demand)

    order = data_source.get_order()
    inventory = Inventory(store)

    allocator = Allocator(inventory, validator)
    allocator.process_orders(order, number_of_orders)

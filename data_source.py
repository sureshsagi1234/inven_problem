'''
Created on Jan 11, 2017

@author: sureshsagiraju
'''
from random import randint, sample


# Data source:
#   There should be a data source capable of generating one or more streams of orders.
#   An order consists of a unique identifier (per stream) we will call the "header", and a demand for between zero and five units each of A,B,C,D, and E, except that there must be at least one unit demanded.
#   A valid order (in whatever format you choose): {"Header": 1, "Lines": {"Product": "A", "Quantity": "1"},{"Product": "C", "Quantity": "4"}}
#   An invalid order: {"Header": 1, "Lines": {"Product": "B", "Quantity": "0"}}
#   Another invalid order: {"Header": 1, "Lines": {"Product": "D", "Quantity": "6"}}
#   Feel free to identify streams as you'd like.


class DataSource(object):

    '''
       streams - number of streams to genrate orders
       valid_products - list of valid products for orders
       min_demand - minimum number of product count in orders
       max_demand - maximum number of product count in orders 
    '''

    def __init__(self, streams, valid_product, min_demand, max_demand):
        self.streams = streams
        self.valid_product = valid_product
        self.min_demand = min_demand
        self.max_demand = max_demand

    '''
        generator which generates random orders
    '''

    def get_order(self):
        headid = 0
        while True:

            for i in range(self.streams):
                order = dict()
                order['stream_id'] = i
                order['Header'] = headid
                order['Lines'] = self.get_lines()
                yield order

            headid += 1

    '''
        creates random lines in order
    '''

    def get_lines(self):
        # get random number of products from list
        number_of_lines = randint(1, len(self.valid_product))
        random_products_index = sorted(
            sample(range(0, len(self.valid_product)), number_of_lines))
        Lines = []
        for i in random_products_index:
            line = {}
            line["Product"] = self.valid_product[i]
            line["Quantity"] = randint(self.min_demand, self.max_demand)
            Lines.append(line)
        return Lines


if __name__ == "__main__":
    # quick tests
    ds = DataSource(3, ['A', 'B', 'C', 'D', 'E'], 1, 5)
    # print ds.get_lines()
    order = ds.get_order()
    for i in range(10):
        print order.next()

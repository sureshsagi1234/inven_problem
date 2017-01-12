'''
Created on Jan 11, 2017

@author: sureshsagiraju
'''

import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG)


class Allocator(object):
    '''
    classdocs
    '''

    def __init__(self, inventory, validator):
        '''
        Constructor
        '''
        self.inventory = inventory
        self.validator = validator

    def process_orders(self, orders, order_count):

        for i in xrange(order_count):

            order = orders.next()
            logging.info("-----------processing order--------")
            logging.info(order)
            logging.info("----------------------------------")
            if self.validator.validate_order(order):
                logging.info("**Valid order**")

            else:
                logging.info("**Invalid order**\n\n")
                continue

            if self.inventory.check_inventory_is_emptry():
                logging.info("***Inventory empty***")
                break

            lines = order['Lines']

            logging.info("inventory before allocation")
            logging.info("----------------------------")
            logging.info(self.inventory.get_inventory())
            logging.info("----------------------------")

            logging.info("actual order  -->" + str(lines))

            back_order_lines = []
            allocated_order_lines = []

            for line in lines:
                back_order = {}
                allocated_order = {}
                allocated_order['Product'] = back_order[
                    'Product'] = line['Product']
                back_order['Quantity'], allocated_order['Quantity'] = self.inventory.allocate(
                    line['Product'], line['Quantity'])
                back_order_lines.append(back_order)
                allocated_order_lines.append(allocated_order)

            logging.info("allocated order -->" + str(allocated_order_lines))
            logging.info("back order     -->" + str(back_order_lines))

            logging.info("inventory after allocation ")
            logging.info("----------------------------")
            logging.info(self.inventory.get_inventory())
            logging.info("----------------------------\n\n")


if __name__ == "__main__":

    # quick unit tests
    pass

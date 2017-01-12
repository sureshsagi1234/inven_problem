'''
Created on Jan 11, 2017

@author: sureshsagiraju
'''


class Validator(object):
    '''
    class to validate orders
    '''

    def __init__(self, valid_products, min_demand, max_demand):
        '''
        Constructor
        '''
        self.valid_products = valid_products
        self.min_demand = min_demand
        self.max_demand = max_demand

        self.order_elements = ['stream_id',  'Header', 'Lines']
        self.line_elements = ['Product', 'Quantity']
        self.orderid = []

    '''
        validate the order if it satisfies the rules
    '''

    def validate_order(self, order):

        # Check order dict have valid elements
        if not sorted(order.keys()) == sorted(self.order_elements):
            return False
        # Check if order can be uniquely identified
        generated_id = self.generate_order_id(
            order['stream_id'], order['Header'])

        if generated_id not in self.orderid:
            self.orderid.append(generated_id)
        else:
            return False

        # Check if order lines have valid products and quantity
        for item in order['Lines']:
            if not sorted(item.keys()) == sorted(self.line_elements):
                return False

            if item['Product'] not in self.valid_products:
                return False

            if not self.min_demand <= item['Quantity'] <= self.max_demand:
                return False

        return True

    '''
        function to generate unique id to identify the order 
    '''

    def generate_order_id(self, stream_id, header_id):
        return str(stream_id) + str(header_id)


if __name__ == "__main__":
    # quick_tests
    val = Validator(['A', 'B', 'C', 'D', 'E'], 1, 5)
    order = {'stream_id': 0, 'Lines': [{'Product': 'B', 'Quantity': 4}, {'Product': 'C', 'Quantity': 3}, {
        'Product': 'D', 'Quantity': 1}, {'Product': 'E', 'Quantity': 2}], 'Header': 0}
    print val.validate_order(order)
    print val.validate_order(order)

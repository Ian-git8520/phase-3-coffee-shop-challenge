from order import Order

class Coffee:

    all = []  # track all coffees

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # name must be string and at least 3 characters
        if type(value) is not str:
            raise Exception("Name must be a string")
        if len(value) < 3:
            raise Exception("Coffee name must be at least 3 characters")
        self._name = value

    # all orders for this coffee
    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    # all customers who bought this coffee (unique)
    def customers(self):
        customers = []
        for order in self.orders():
            if order.customer not in customers:
                customers.append(order.customer)
        return customers

    # count all orders
    def num_orders(self):
        return len(self.orders())

    # get average price
    def average_price(self):
        orders = self.orders()
        if len(orders) == 0:
            return 0
        
        total = 0
        for order in orders:
            total += order.price

        return total / len(orders)

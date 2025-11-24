from order import Order

class Customer:

    all = []  # to keep track of all customers

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # name must be a string between 1 and 15 characters
        if type(value) is not str:
            raise Exception("Name must be a string")
        if len(value) < 1 or len(value) > 15:
            raise Exception("Name must be between 1 and 15 characters")
        self._name = value

    # return all orders for this customer
    def orders(self):
        return [order for order in Order.all if order.customer is self]

    # return all coffees this customer has ordered
    def coffees(self):
        coffees = []
        for order in self.orders():
            if order.coffee not in coffees:
                coffees.append(order.coffee)
        return coffees

    # create a new order
    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    # find who spent the most money on a specific coffee
    @classmethod
    def most_aficionado(cls, coffee):
        highest_spender = None
        highest_amount = 0

        for customer in cls.all:
            total = 0
            for order in customer.orders():
                if order.coffee == coffee:
                    total += order.price

            if total > highest_amount:
                highest_amount = total
                highest_spender = customer

        return highest_spender

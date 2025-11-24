class Order:

    all = []  # track all orders

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        # avoid circular import problems
        from customer import Customer
        if not isinstance(value, Customer):
            raise Exception("customer must be a Customer instance")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise Exception("coffee must be a Coffee instance")
        self._coffee = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        # price must be a number between 1 and 10
        if type(value) not in [int, float]:
            raise Exception("Price must be a number")
        if value < 1 or value > 10:
            raise Exception("Price must be between 1 and 10")
        self._price = value

# customer.py
from typing import List, Optional

class Customer:
    _all = []

    def __init__(self, name: str):
        self.name = name  # triggers validation
        Customer._all.append(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string")
        value = value.strip()
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name length must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        from order import Order
        return [o for o in Order.all() if o.customer is self]

    def coffees(self):
        # unique list of coffees this customer has ordered
        seen = []
        for o in self.orders():
            if o.coffee not in seen:
                seen.append(o.coffee)
        return seen

    def create_order(self, coffee, price: float):
        from order import Order
        # Validate coffee is Coffee instance inside Order constructor
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """
        Customer who spent the most total on the provided coffee.
        Returns Customer instance or None if no orders exist for that coffee.
        """
        from order import Order
        # aggregate spending per customer for this coffee
        totals = {}
        for o in Order.all():
            if o.coffee is coffee:
                totals[o.customer] = totals.get(o.customer, 0.0) + o.price

        if not totals:
            return None

        # find customer with max spending; if tie, first encountered
        best_customer = max(totals.items(), key=lambda kv: kv[1])[0]
        return best_customer

    @classmethod
    def all(cls) -> List['Customer']:
        return list(cls._all)

    def __repr__(self):
        return f"<Customer {self.name}>"

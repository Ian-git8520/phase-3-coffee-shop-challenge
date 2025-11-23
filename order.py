# order.py
from typing import List

class Order:
    _all = []

    def __init__(self, customer, coffee, price: float):
        from customer import Customer
        from coffee import Coffee

        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        try:
            price = float(price)
        except Exception:
            raise TypeError("price must be a number")

        if not (1.0 <= price <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0 inclusive")

        self._customer = customer
        self._coffee = coffee
        self._price = price

        Order._all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        try:
            value = float(value)
        except Exception:
            raise TypeError("price must be a number")

        if not (1.0 <= value <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0 inclusive")
        self._price = value

    @classmethod
    def all(cls) -> List['Order']:
        return list(cls._all)

    def __repr__(self):
        return f"<Order {self.customer.name} - {self.coffee.name} @ {self.price:.2f}>"

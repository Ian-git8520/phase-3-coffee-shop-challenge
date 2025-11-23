# coffee.py
from typing import List, Optional

class Coffee:
    _all = []

    def __init__(self, name: str):
        self.name = name  # triggers validation
        Coffee._all.append(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string")
        value = value.strip()
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = value

    def orders(self):
        from order import Order
        return [o for o in Order.all() if o.coffee is self]

    def customers(self):
        seen = []
        for o in self.orders():
            if o.customer not in seen:
                seen.append(o.customer)
        return seen

    def num_orders(self) -> int:
        return len(self.orders())

    def average_price(self) -> Optional[float]:
        orders = self.orders()
        if not orders:
            return None
        total = sum(o.price for o in orders)
        return total / len(orders)

    @classmethod
    def all(cls) -> List['Coffee']:
        return list(cls._all)

    def __repr__(self):
        return f"<Coffee {self.name}>"

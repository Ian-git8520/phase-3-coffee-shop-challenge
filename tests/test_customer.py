
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def setup_function():
    Customer._all.clear()
    Coffee._all.clear()
    Order._all.clear()

def test_customer_orders_and_coffees():
    alice = Customer("Alice")
    latte = Coffee("Latte")
    mocha = Coffee("Mocha")
    alice.create_order(latte, 4.0)
    alice.create_order(mocha, 5.0)
    assert len(alice.orders()) == 2
    assert set(alice.coffees()) == {latte, mocha}

def test_most_aficionado():
    c1 = Customer("A")
    c2 = Customer("B")
    c = Coffee("Dark")
    c1.create_order(c, 3.0)
    c1.create_order(c, 4.0)
    c2.create_order(c, 6.0)  # c2 spent more (6.0 vs 7.0) -> actually c1 spent 7.0 > 6.0
    # so c1 should be most aficionado
    assert Customer.most_aficionado(c) is c1

def test_most_aficionado_none():
    c = Coffee("Solo")
    assert Customer.most_aficionado(c) is None

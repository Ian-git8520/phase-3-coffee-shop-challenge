
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_init():
    cust = Customer("Ian")
    coffee = Coffee("Latte")
    order = Order(cust, coffee, 5.0)

    assert order.customer == cust
    assert order.coffee == coffee
    assert order.price == 5.0

def test_invalid_price():
    c = Customer("Mary")
    cf = Coffee("Mocha")

    with pytest.raises(Exception):
        Order(c, cf, 0)

    with pytest.raises(Exception):
        Order(c, cf, 15)


import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def setup_function():
    Customer._all.clear()
    Coffee._all.clear()
    Order._all.clear()

def test_order_validation():
    c = Customer("Tim")
    coffee = Coffee("Mocha")
    with pytest.raises(TypeError):
        Order("not a customer", coffee, 3.0)
    with pytest.raises(TypeError):
        Order(c, "not a coffee", 3.0)
    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)
    o = Order(c, coffee, 3.25)
    assert o.customer is c
    assert o.coffee is coffee
    assert abs(o.price - 3.25) < 1e-6

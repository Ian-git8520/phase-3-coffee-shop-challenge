
import pytest
from customer import Customer
from coffee import Coffee

def test_customer_name():
    c = Customer("Ian")
    assert c.name == "Ian"

def test_invalid_name():
    with pytest.raises(Exception):
        Customer("")

    with pytest.raises(Exception):
        Customer("ThisNameIsWayTooLong")

def test_create_order():
    c = Customer("Mary")
    coffee = Coffee("Latte")
    order = c.create_order(coffee, 5.0)

    assert order in c.orders()
    assert coffee in c.coffees()

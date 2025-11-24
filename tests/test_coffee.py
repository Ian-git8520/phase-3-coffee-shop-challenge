
from customer import Customer
from coffee import Coffee

def test_coffee_name():
    c = Coffee("Mocha")
    assert c.name == "Mocha"

def test_coffee_orders_and_customers():
    cust1 = Customer("Ian")
    cust2 = Customer("Mary")
    latte = Coffee("Latte")

    cust1.create_order(latte, 5.0)
    cust2.create_order(latte, 6.0)

    assert len(latte.orders()) == 2
    assert len(latte.customers()) == 2

def test_average_price():
    c1 = Customer("A")
    c2 = Customer("B")
    espresso = Coffee("Espresso")

    c1.create_order(espresso, 4.0)
    c2.create_order(espresso, 6.0)

    assert espresso.average_price() == 5.0


from customer import Customer
from coffee import Coffee
from order import Order

def setup_function():
    Customer._all.clear()
    Coffee._all.clear()
    Order._all.clear()

def test_coffee_aggregates():
    alice = Customer("A")
    bob = Customer("B")
    espresso = Coffee("Espresso")
    alice.create_order(espresso, 3.0)
    alice.create_order(espresso, 4.0)
    bob.create_order(espresso, 5.0)
    assert espresso.num_orders() == 3
    avg = espresso.average_price()
    assert abs(avg - ((3.0 + 4.0 + 5.0)/3)) < 1e-6
    assert set(espresso.customers()) == {alice, bob}

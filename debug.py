# debug.py
from customer import Customer
from coffee import Coffee
from order import Order

def reset_all():
    Customer._all.clear()
    Coffee._all.clear()
    Order._all.clear()

if __name__ == "__main__":
    reset_all()
    # create customers
    alice = Customer("Alice")
    bob = Customer("Bob")

    # create coffees
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    # orders
    alice.create_order(espresso, 3.5)
    alice.create_order(espresso, 2.0)
    bob.create_order(espresso, 4.5)
    bob.create_order(latte, 5.0)

    # outputs
    print("All customers:", Customer.all())
    print("All coffees:", Coffee.all())
    from order import Order as O
    print("All orders:", O.all())

    print("Espresso orders:", espresso.orders())
    print("Espresso customers:", espresso.customers())
    print("Espresso num orders:", espresso.num_orders())
    print("Espresso average price:", espresso.average_price())

    print("Alice coffees:", alice.coffees())
    print("Most aficionado for Espresso:", Customer.most_aficionado(espresso))

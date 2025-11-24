# debug.py

from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
c1 = Customer("Ian")
c2 = Customer("Mary")

# Create coffees
latte = Coffee("Latte")
mocha = Coffee("Mocha")

# Create orders
o1 = c1.create_order(latte, 5.0)
o2 = c1.create_order(mocha, 6.0)
o3 = c2.create_order(latte, 4.5)

# Try printing
print("Ian's Orders:", c1.orders())
print("Ian's Coffees:", c1.coffees())
print("Latte Orders:", latte.orders())
print("Latte Customers:", latte.customers())
print("Latte average price:", latte.average_price())

print("Most aficionado for Latte:", Customer.most_aficionado(latte))

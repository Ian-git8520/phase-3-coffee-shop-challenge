Coffee Shop Domain Model

This project models a Coffee Shop domain using Object-Oriented Programming in Python.

Project Structure
coffee_shop/
│
├── customer.py      # Customer class definition
├── coffee.py        # Coffee class definition
├── order.py         # Order class definition
├── debug.py         # Testing and debugging file
└── README.md        # This file
Setup Instructions

Create virtual environment:

bash   pipenv install
   pipenv shell

Install pytest (for testing):

bash   pipenv install pytest
Domain Model
The coffee shop has three main entities:
1. Customer




orders() - Returns all orders for this customer
coffees() - Returns unique list of coffees ordered
create_order(coffee, price) - Creates a new order
most_aficionado(coffee) - Class method that returns the customer who spent the most on a given coffee



2. Coffee

Attributes: name (string, minimum 3 characters)
Methods:

orders() - Returns all orders for this coffee
customers() - Returns unique list of customers who ordered this coffee
num_orders() - Returns total number of orders for this coffee
average_price() - Returns average price of this coffee



3. Order

Attributes:

customer (Customer instance)
coffee (Coffee instance)
price (float, between 1.0 and 10.0)


Class Variable:

all_orders - Stores all order instances (single source of truth)



Relationships

A Customer can place many Orders
A Coffee can have many Orders
An Order belongs to one Customer and one Coffee
Customer ↔ Order ↔ Coffee (many-to-many through Order)

Running the Code
To test the implementation:
bashpython debug.py
This will:

Create sample customers, coffees, and orders
Test all methods and relationships
Validate input constraints
Display results

Key Features
 Input validation for all attributes
 Property decorators for controlled access
 Single source of truth (all orders stored in Order.all_orders)
 Relationship methods to navigate between objects
 Aggregate methods (counting, averaging)
 Class method for finding top customer




Author
[IAN NJENGA]

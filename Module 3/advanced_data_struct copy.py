# Mini system to process customer orders.
from enum import Enum
from collections import namedtuple, deque, Counter


class Status(Enum):
    RECEIVED = 1
    PROCESSING = 2
    COMPLETED = 3


Customer = namedtuple('Customer', ['name', 'email'])
Order = namedtuple('Order', ['customer', 'product', 'status'])

orders = deque()

product_counter = Counter()

def take_order():
    name = input("Enter customer's name: ")
    email = input("Enter customer's email: ")
    product = input("Enter product's name: ")
    return Order(Customer(name, email), product, Status.RECEIVED)

#Simulate orders

orders.extend([
    Order(Customer("John Doe", "john@example.com"), "Watch", Status.RECEIVED),
    Order(Customer("Jane Smith", "jane@example.com"), "Gadget", Status.RECEIVED)

])


while True:
    order_input = input("New order (yes/no?")
    if order_input.lower() == 'yes':
        orders.append(take_order())
    elif order_input.lower() == 'no':
        break

while orders:
    current_order = orders.popleft()
    print(f"\nProcessing order from {current_order.customer.name}")

    current_order = current_order._replace(status = Status.PROCESSING)

    product_counter[current_order.product] += 1

    current_order = current_order._replace(status = Status.COMPLETED)
    print(f"Order from {current_order.customer.name} for {current_order.product} completed")


print("\nFrequency of Ordered Products: ")
for product, count in product_counter.items():
    print(f"{product}: ordered {count} times")

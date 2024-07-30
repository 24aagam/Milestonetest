
from datetime import datetime

class Order:
    def __init__(self, order_id, customer_name, products):
        self.order_id = order_id
        self.customer_name = customer_name
        self.products = products
        self.order_date = datetime.now()

    def __str__(self):
        return f"Order({self.order_id}, {self.customer_name}, {self.products}, {self.order_date})"

def create_order(order_list, order):
    """Add an order to the order list."""
    order_list.append(order)

def cancel_order(order_list, order_id):
    """Cancel an order from the order list by its ID."""
    order_list[:] = [order for order in order_list if order.order_id != order_id]

def list_orders(order_list):
    """List all orders."""
    return order_list


class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product({self.product_id}, {self.name}, {self.price}, {self.quantity})"

def add_product(product_list, product):
    """Add a product to the product list."""
    product_list.append(product)

def remove_product(product_list, product_id):
    """Remove a product from the product list by its ID."""
    product_list[:] = [product for product in product_list if product.product_id != product_id]

def update_product_quantity(product_list, product_id, quantity):
    """Update the quantity of a product in the product list."""
    for product in product_list:
        if product.product_id == product_id:
            product.quantity = quantity
            break

class CustomerNotFoundException(Exception):
    def __init__(self, customer_id):
        super().__init__(f"Customer with ID {customer_id} not found")

class ProductNotFoundException(Exception):
    def __init__(self, product_id):
        super().__init__(f"Product with ID {product_id} not found")

class OrderNotFoundException(Exception):
    def __init__(self, order_id):
        super().__init__(f"Order with ID {order_id} not found")

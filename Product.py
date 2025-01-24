class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.status = "active"

    def add_product(self):
        print(f"Product {self.name} added successfully!")

    def update_product(self, name, price):
        self.name = name
        self.price = price
        print(f"Product {self.product_id} updated successfully!")

    def suspend_product(self):
        self.status = "suspended"
        print(f"Product {self.name} has been suspended.")

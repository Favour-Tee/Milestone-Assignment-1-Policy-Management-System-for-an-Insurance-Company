from Policyholder import Policyholder
from Product import Product
from Payment import Payment

# Step 1: Create two policyholders
policyholder1 = Policyholder("Favour", 101)
policyholder2 = Policyholder("Chigozie", 102)

# Register the policyholders
policyholder1.register_policyholder()
policyholder2.register_policyholder()

# Step 2: Create a product
product1 = Product(201, "Health Insurance", 5000)
product1.add_product()

# Step 3: Process payments for the product
payment1 = Payment(policyholder1.name, product1.price)
payment2 = Payment(policyholder2.name, product1.price)

payment1.process_payment()
payment2.process_payment()

# Step 4: Display account details
print("\n--- Policyholder Account Details ---")
print(f"Name: {policyholder1.name}, Policy ID: {policyholder1.policy_id}, Status: {policyholder1.status}")
print(f"Name: {policyholder2.name}, Policy ID: {policyholder2.policy_id}, Status: {policyholder2.status}")

print("\n--- Product Details ---")
print(f"Product Name: {product1.name}, Product ID: {product1.product_id}, Price: {product1.price}")

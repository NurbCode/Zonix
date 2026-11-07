from decimal import Decimal

from apps.catalog.product import Product
from apps.catalog.category import Category

iphone = Product(name="iPhone", price=Decimal("999.99"), quantity=10)
macbook = Product(name="MacBook", price=Decimal("1999.99"), quantity=5)


print("Initial information:")
print(f"iPhone: {iphone.name}, Price: {iphone.price}, Quantity: {iphone.quantity}")

print("\nChecking availability:")
print(f"iPhone available: {iphone.is_available()}")

print("\nSelling products:")
iphone.sell(3)

print(f"Remaining stock: {iphone.quantity}")

print("\nRestocking:")
iphone.restock(5)

print(f"Updated stock: {iphone.quantity}")

print("\nUpdating price:")
iphone.update_price(Decimal("480000.00"))

print(f"New price: {iphone.price}")
print(f"iPhone: {iphone.name}, Price: {iphone.price}, Quantity: {iphone.quantity}")

smartphones = Category("Smartphones")

iphone = Product("iPhone 17", Decimal("500000"), 10)
samsung = Product("Samsung Galaxy S25", Decimal("450000"), 5)
google_pixel = Product("Google Pixel", Decimal("400000"), 7)

# Add products to category
smartphones.add_product(iphone)
smartphones.add_product(samsung)
smartphones.add_product(google_pixel)

# Display category
print(f"\nCategory: {smartphones.name}")

for product in smartphones.get_products():
    print(
        f"Product: {product.name} | "
        f"Price: {product.price} | "
        f"Quantity: {product.quantity}"
    )

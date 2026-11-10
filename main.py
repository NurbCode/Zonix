from decimal import Decimal

from apps.catalog.category import Category
from apps.catalog.physical_product import PhysicalProduct
from apps.catalog.digital_product import DigitalProduct


# Create products
iphone = PhysicalProduct(
    name="iPhone 17",
    price=Decimal("500000"),
    quantity=10,
    weight_kg=Decimal("0.2")
)

samsung = PhysicalProduct(
    name="Samsung Galaxy S25",
    price=Decimal("450000"),
    quantity=5,
    weight_kg=Decimal("0.19")
)

ebook = DigitalProduct(
    name="Python Programming Ebook",
    price=Decimal("5000"),
    quantity=100,
    file_size_mb=Decimal("15.5"),
    download_url="https://example.com/ebook"
)


# Create category
smartphones = Category("Smartphones")

smartphones.add_product(iphone)
smartphones.add_product(samsung)


# Display category
print("=== CATEGORY ===")
print(smartphones)

for product in smartphones.get_products():
    print(product)


# Display product information
print("\n=== PRODUCT INFORMATION ===")
print(iphone.get_product_info())
print()
print(ebook.get_product_info())


# Demonstrate polymorphism
print("\n=== POLYMORPHISM ===")

products = [iphone, samsung, ebook]

for product in products:
    print(product.get_product_info())
    print("-" * 30)


# Demonstrate encapsulation
print("\n=== ENCAPSULATION ===")

print(f"Current price: {iphone.price}")
print(f"Current stock: {iphone.quantity}")

iphone.price = Decimal("480000")
iphone.restock(5)
iphone.sell(2)

print(f"Updated price: {iphone.price}")
print(f"Updated stock: {iphone.quantity}")


# Demonstrate special methods
print("\n=== SPECIAL METHODS ===")

print(str(iphone))
print(repr(iphone))

print(str(smartphones))
print(repr(smartphones))

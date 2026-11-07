from apps.catalog.product import Product


class Category:
    def __init__(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Category name cannot be empty.")

        self.name = name
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added.")

        if product in self.products:
            raise ValueError("Product already exists in this category.")

        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        if product not in self.products:
            raise ValueError("Product not found in this category.")

        self.products.remove(product)

    def get_products(self) -> list[Product]:
        return self.products.copy()

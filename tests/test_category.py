import unittest
from decimal import Decimal

from apps.catalog.category import Category
from apps.catalog.physical_product import PhysicalProduct


class TestCategory(unittest.TestCase):

    def setUp(self) -> None:
        self.category = Category("Electronics")

        self.product = PhysicalProduct(
            name="Laptop",
            price=Decimal("500000"),
            quantity=10,
            weight_kg=Decimal("2.5")
        )

    # Category validation
    def test_empty_category_name(self) -> None:
        with self.assertRaises(ValueError):
            Category("")

    # Adding products
    def test_add_product(self) -> None:
        self.category.add_product(self.product)

        self.assertEqual(len(self.category.products), 1)
        self.assertIn(self.product, self.category.products)

    def test_cannot_add_invalid_object(self) -> None:
        with self.assertRaises(TypeError):
            self.category.add_product("Laptop")

    def test_cannot_add_duplicate_product(self) -> None:
        self.category.add_product(self.product)

        with self.assertRaises(ValueError):
            self.category.add_product(self.product)

    # Removing products
    def test_remove_product(self) -> None:
        self.category.add_product(self.product)
        self.category.remove_product(self.product)

        self.assertNotIn(self.product, self.category.products)

    def test_cannot_remove_missing_product(self) -> None:
        with self.assertRaises(ValueError):
            self.category.remove_product(self.product)

    # Getting products
    def test_get_products_returns_copy(self) -> None:
        self.category.add_product(self.product)

        products = self.category.get_products()
        products.clear()

        self.assertEqual(len(self.category.products), 1)

    # Special methods
    def test_category_string_representation(self) -> None:
        self.assertEqual(
            str(self.category),
            "Electronics (0 products)"
        )

    def test_category_repr(self) -> None:
        self.assertEqual(
            repr(self.category),
            "Category(name='Electronics', products=0)"
        )


if __name__ == "__main__":
    unittest.main()

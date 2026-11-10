import unittest
from decimal import Decimal

from apps.catalog.physical_product import PhysicalProduct
from apps.catalog.digital_product import DigitalProduct


class TestProductValidation(unittest.TestCase):

    def setUp(self) -> None:
        self.product = PhysicalProduct(
            name="Laptop",
            price=Decimal("500000"),
            quantity=10,
            weight_kg=Decimal("2.5")
        )

    # Name validation
    def test_empty_product_name(self) -> None:
        with self.assertRaises(ValueError):
            PhysicalProduct(
                name="",
                price=Decimal("1000"),
                quantity=5,
                weight_kg=Decimal("1.0")
            )

    # Price validation
    def test_negative_price(self) -> None:
        with self.assertRaises(ValueError):
            PhysicalProduct(
                name="Laptop",
                price=Decimal("-100"),
                quantity=5,
                weight_kg=Decimal("1.0")
            )

    def test_price_must_be_decimal(self) -> None:
        with self.assertRaises(TypeError):
            PhysicalProduct(
                name="Laptop",
                price=1000,
                quantity=5,
                weight_kg=Decimal("1.0")
            )

    # Quantity validation
    def test_negative_quantity(self) -> None:
        with self.assertRaises(ValueError):
            PhysicalProduct(
                name="Laptop",
                price=Decimal("1000"),
                quantity=-5,
                weight_kg=Decimal("1.0")
            )

    def test_quantity_must_be_integer(self) -> None:
        with self.assertRaises(TypeError):
            PhysicalProduct(
                name="Laptop",
                price=Decimal("1000"),
                quantity=5.5,
                weight_kg=Decimal("1.0")
            )

    # Stock operations
    def test_cannot_sell_more_than_available(self) -> None:
        with self.assertRaises(ValueError):
            self.product.sell(11)

    def test_cannot_sell_zero_products(self) -> None:
        with self.assertRaises(ValueError):
            self.product.sell(0)

    def test_cannot_restock_negative_amount(self) -> None:
        with self.assertRaises(ValueError):
            self.product.restock(-5)

    def test_sell_reduces_quantity(self) -> None:
        self.product.sell(3)
        self.assertEqual(self.product.quantity, 7)

    def test_restock_increases_quantity(self) -> None:
        self.product.restock(5)
        self.assertEqual(self.product.quantity, 15)

    # Physical product validation
    def test_weight_must_be_positive(self) -> None:
        with self.assertRaises(ValueError):
            PhysicalProduct(
                name="Laptop",
                price=Decimal("1000"),
                quantity=5,
                weight_kg=Decimal("0")
            )

    # Digital product validation
    def test_file_size_must_be_positive(self) -> None:
        with self.assertRaises(ValueError):
            DigitalProduct(
                name="Ebook",
                price=Decimal("1000"),
                quantity=10,
                file_size_mb=Decimal("-5"),
                download_url="https://example.com"
            )

    def test_download_url_cannot_be_empty(self) -> None:
        with self.assertRaises(ValueError):
            DigitalProduct(
                name="Ebook",
                price=Decimal("1000"),
                quantity=10,
                file_size_mb=Decimal("15"),
                download_url=""
            )


if __name__ == "__main__":
    unittest.main()

import unittest
from decimal import Decimal

from apps.catalog.pricing import (
    apply_discount,
    calculate_total,
    is_available,
)


class TestPricing(unittest.TestCase):
    def test_calculate_total(self) -> None:
        self.assertEqual(
            calculate_total(Decimal("12.50"), 4),
            Decimal("50.00"),
        )

    def test_calculate_total_with_zero_quantity(self) -> None:
        self.assertEqual(
            calculate_total(Decimal("12.50"), 0),
            Decimal("0.00"),
        )

    def test_calculate_total_rejects_negative_price(self) -> None:
        with self.assertRaises(ValueError):
            calculate_total(Decimal("-1.00"), 2)

    def test_calculate_total_rejects_negative_quantity(self) -> None:
        with self.assertRaises(ValueError):
            calculate_total(Decimal("1.00"), -2)

    def test_apply_discount(self) -> None:
        self.assertEqual(
            apply_discount(Decimal("100.00"), Decimal("15")),
            Decimal("85.00"),
        )

    def test_apply_zero_discount(self) -> None:
        self.assertEqual(
            apply_discount(Decimal("12.34"), Decimal("0")),
            Decimal("12.34"),
        )

    def test_apply_full_discount(self) -> None:
        self.assertEqual(
            apply_discount(Decimal("12.34"), Decimal("100")),
            Decimal("0.00"),
        )

    def test_discount_rounds_half_up_to_two_places(self) -> None:
        self.assertEqual(
            apply_discount(Decimal("10.05"), Decimal("10")),
            Decimal("9.05"),
        )

    def test_apply_discount_rejects_negative_total(self) -> None:
        with self.assertRaises(ValueError):
            apply_discount(Decimal("-1.00"), Decimal("10"))

    def test_apply_discount_rejects_negative_percentage(self) -> None:
        with self.assertRaises(ValueError):
            apply_discount(Decimal("10.00"), Decimal("-1"))

    def test_apply_discount_rejects_percentage_over_100(self) -> None:
        with self.assertRaises(ValueError):
            apply_discount(Decimal("10.00"), Decimal("101"))

    def test_is_available_for_positive_quantity(self) -> None:
        self.assertTrue(is_available(3))

    def test_is_not_available_for_zero_quantity(self) -> None:
        self.assertFalse(is_available(0))

    def test_is_available_rejects_negative_quantity(self) -> None:
        with self.assertRaises(ValueError):
            is_available(-1)


if __name__ == "__main__":
    unittest.main()

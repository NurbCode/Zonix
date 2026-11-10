from decimal import Decimal

from apps.catalog.product import Product


class PhysicalProduct(Product):
    def __init__(
        self,
        name: str,
        price: Decimal,
        quantity: int,
        weight_kg: Decimal
    ) -> None:
        super().__init__(name, price, quantity)

        if not isinstance(weight_kg, Decimal):
            raise TypeError("Weight must be a Decimal.")

        if weight_kg <= 0:
            raise ValueError("Weight must be positive.")

        self._weight_kg = weight_kg

    @property
    def weight_kg(self) -> Decimal:
        return self._weight_kg

    def __str__(self) -> str:
        return (
            f"{super().__str__()} "
            f"(Weight: {self.weight_kg} kg)"
        )

    def get_product_info(self) -> str:
        return (
            f"{self._get_base_product_info()}\n"
            f"Type: Physical\n"
            f"Weight: {self.weight_kg} kg"
        )

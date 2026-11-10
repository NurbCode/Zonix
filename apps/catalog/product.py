from decimal import Decimal
from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(
        self,
        name: str,
        price: Decimal,
        quantity: int
    ) -> None:
        if not name.strip():
            raise ValueError("Product name cannot be empty.")

        if not isinstance(price, Decimal):
            raise TypeError("Price must be a Decimal.")

        if price < 0:
            raise ValueError("Price cannot be negative.")

        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self._price = price
        self._quantity = quantity

    @property
    def price(self) -> Decimal:
        return self._price

    @price.setter
    def price(self, new_price: Decimal) -> None:
        if not isinstance(new_price, Decimal):
            raise TypeError("Price must be a Decimal.")

        if new_price < 0:
            raise ValueError("Price cannot be negative.")

        self._price = new_price

    @property
    def quantity(self) -> int:
        return self._quantity

    def is_available(self) -> bool:
        return self._quantity > 0

    def update_price(self, new_price: Decimal) -> None:
        self.price = new_price

    def restock(self, amount: int) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int):
            raise TypeError("Restock amount must be an integer.")

        if amount <= 0:
            raise ValueError("Restock amount must be positive.")

        self._quantity += amount

    def sell(self, amount: int) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int):
            raise TypeError("Sale amount must be an integer.")

        if amount <= 0:
            raise ValueError("Sale amount must be positive.")

        if amount > self._quantity:
            raise ValueError("Not enough products in stock.")

        self._quantity -= amount

    def __str__(self) -> str:
        return (
            f"{self.name} — {self.price} ₸ "
            f"(Stock: {self.quantity})"
        )

    def __repr__(self) -> str:
        return (
            f"Product(name={self.name!r}, "
            f"price={self.price!r}, "
            f"quantity={self.quantity!r})"
        )

    def _get_base_product_info(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"Price: {self.price} ₸\n"
            f"Stock: {self.quantity}"
        )

    @abstractmethod
    def get_product_info(self) -> str:
        pass

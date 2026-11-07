from decimal import Decimal

class Product:
    def __init__(
            self,
            name: str,
            price: Decimal,
            quantity: int,
    ):
        self.name = name
        self.price = price
        self.quantity = quantity

    def is_available(self) -> bool:
        return self.quantity > 0

    def update_price(self, new_price: Decimal) -> None:
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.price = new_price

    def restock(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Restock amount must be positive.")

        self.quantity += amount

    def sell(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Sell amount must be positive.")

        if amount > self.quantity:
            raise ValueError("Not enough stock to sell the requested amount.")

        self.quantity -= amount
from decimal import Decimal, ROUND_HALF_UP


def calculate_total(price: Decimal, quantity: int) -> Decimal:
    if price < 0:
        raise ValueError("Price cannot be negative.")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    return price * quantity


def apply_discount(total: Decimal, discount_percentage: Decimal) -> Decimal:
    if total < 0:
        raise ValueError("Total cannot be negative.")

    if not Decimal(0) <= discount_percentage <= Decimal(100):
        raise ValueError("Discount percentage must be between 0 and 100.")

    discount_amount = total * discount_percentage / Decimal(100)

    discounted_total = total - discount_amount

    return discounted_total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def is_available(requested_quantity: int) -> bool:
    if requested_quantity < 0:
        raise ValueError("Requested quantity cannot be negative.")

    return requested_quantity > 0

# Stage 01 — Encapsulation

## Current implementation

`Product` stores price and stock in `_price` and `_quantity`:

- `price` is exposed through a property with a setter that requires a non-negative `Decimal`.
- `quantity` is exposed as a read-only property.
- `restock(amount)` and `sell(amount)` are the supported stock mutation methods. They require positive integers; selling more than the available stock raises `ValueError`.
- The constructor validates the product name, price type and value, and initial quantity type and value.
- `update_price()` delegates to the `price` setter, so it uses the same validation.

`PhysicalProduct` and `DigitalProduct` expose their additional attributes through read-only properties. As usual in Python, underscore-prefixed attributes signal non-public implementation details but do not enforce access restrictions.

## Concepts covered

- Properties and setters.
- Public and non-public attributes.
- Input validation and exceptions.
- Keeping stock changes behind explicit methods.
- Reusing validation to avoid duplicate logic.

## Related files

- `apps/catalog/product.py`
- `apps/catalog/physical_product.py`
- `apps/catalog/digital_product.py`

## Current result

Normal public access prevents direct assignment to `quantity` and validates price assignments. This is a Python interface convention, not strict protection against modifying underscore-prefixed fields. Automated tests for these behaviors are not currently committed.

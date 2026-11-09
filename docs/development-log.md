## Stage 01 — Inheritance, Polymorphism & Abstract Classes

**Date:** 2026-11-09

### Completed

- Implemented `PhysicalProduct` inheriting from `Product`.
- Implemented `DigitalProduct` inheriting from `Product`.
- Added product-specific attributes and properties.
- Implemented method overriding through `get_product_info()`.
- Added polymorphic behavior for different product types.
- Converted `Product` into an abstract base class using `ABC`.
- Added `@abstractmethod` to enforce implementation of `get_product_info()`.
- Added `_get_base_product_info()` to reuse common product information.

### Testing

- `test_inheritance.py`
- `test_polymorphism.py`
- `test_abstract.py`

All three test scenarios were executed successfully.

### Concepts Covered

Inheritance, Polymorphism, Dynamic Dispatch, Abstract Classes, ABC and Method Overriding.
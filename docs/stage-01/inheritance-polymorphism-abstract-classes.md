# Stage 01 — Inheritance, Polymorphism, and Abstract Classes

## Product hierarchy

`Product` in `apps/catalog/product.py` is an abstract base class built on `ABC`. It contains the shared name, price, stock behavior, validation, and common information formatting. Its abstract `get_product_info()` method requires concrete subclasses to provide type-specific details.

```text
Product (abstract)
├── PhysicalProduct
└── DigitalProduct
```

### PhysicalProduct

Adds a positive `Decimal` `weight_kg`, exposed through a read-only property. Its `get_product_info()` includes the common product details and weight. Its string representation also includes the weight.

### DigitalProduct

Adds a positive `Decimal` `file_size_mb` and a non-empty `download_url`, both exposed through read-only properties. Its `get_product_info()` includes the common details, file size, and download URL. Its string representation includes the file size.

Both subclasses call `super().__init__()` and inherit the base price and stock operations, including `sell()`, `restock()`, `is_available()`, and `update_price()`.

## Polymorphism

Code can call `get_product_info()` on a `Product` reference and receive details from the concrete product type. Python dispatches to the subclass implementation at runtime. Both implementations reuse `_get_base_product_info()` for shared fields.

## Related files

```text
apps/catalog/
  product.py
  physical_product.py
  digital_product.py
```

## Current status

Inheritance, overriding, runtime dispatch, and the abstract product interface are implemented. The repository does not currently contain the `test_inheritance.py`, `test_polymorphism.py`, or `test_abstract.py` files mentioned in earlier notes, so automated test coverage is not established by the checked-in project.

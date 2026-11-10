# Stage 01 — Categories and Composition

## Overview

The catalog uses `Category` to group product objects. A category stores references to products; adding a product does not transfer ownership or copy the product itself.

## Current implementation

`apps/catalog/category.py` defines `Category` with:

- A non-empty `name`.
- A `products` list annotated as `list[Product]`.
- `add_product(product)`, which accepts `Product` instances and rejects duplicates.
- `remove_product(product)`, which rejects products that are not members.
- `get_products()`, which returns a shallow copy of the list.
- `__str__()` and `__repr__()` representations.

`Product` is abstract, so categories contain concrete `PhysicalProduct` or `DigitalProduct` instances. The collection is shallow-copied: callers cannot change category membership by editing the returned list, but the product objects themselves remain shared references. The `products` attribute is also directly accessible in the current implementation.

## Concepts covered

- Composition and object references.
- Type annotations for collections.
- `isinstance()` checks.
- List operations and shallow copies.
- Exceptions for invalid membership operations.
- Python special methods `__str__()` and `__repr__()`.

## Related files

```text
apps/catalog/
  category.py
  product.py
  physical_product.py
  digital_product.py
```

## Current result

Products can be grouped by category, removed, and listed without exposing the category's list through `get_products()`. There is no automated category test file in the repository yet.

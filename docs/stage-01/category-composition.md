# Stage 01 — Category & Composition

## Overview

In this step, we introduced the `Category` class and explored the concept of Composition in Object-Oriented Programming (OOP).

The goal was to group products into categories and establish relationships between Python objects.

## What We Implemented

### 1. Category Class

Created `category.py` with the following attributes and methods:

- `name` — category name.
- `products` — list of Product objects.
- `add_product()` — adds a product to the category.
- `remove_product()` — removes a product from the category.
- `get_products()` — returns a copy of the product list.

### 2. Composition

Learned how one object can contain references to other objects.

In Zonix:

- A Category contains multiple Product objects.
- Products maintain their own attributes and methods.
- Category provides a way to organize related products.

### 3. Python Concepts

During this step, we explored:

- `list[Product]` — type hints for lists of objects.
- `isinstance()` — checking object types.
- `append()` and `remove()` — list operations.
- `copy()` — creating a shallow copy of a list.
- `raise` — raising exceptions for invalid operations.

## Project Structure

```text
apps/
└── catalog/
    ├── __init__.py
    ├── pricing.py
    ├── product.py
    └── category.py
```

## Result

Zonix now supports product categorization through the `Category` class.

Products can be added to and removed from categories, while retaining their own independent behavior.

## Next Step

Explore Python special methods:

- `__str__()`
- `__repr__()`

These methods will improve how Product and Category objects are represented and displayed.
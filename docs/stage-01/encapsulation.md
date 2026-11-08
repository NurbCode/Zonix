# Stage 01 — Encapsulation

## Overview

Implemented Encapsulation in the Product class to control access to internal object attributes.

## What Changed

- Replaced public `price` attribute with `_price`.
- Replaced public `quantity` attribute with `_quantity`.
- Added `@property` for controlled attribute access.
- Added `@price.setter` to validate price changes.
- Made `quantity` read-only through the public interface.
- Updated `update_price()` to use the price setter.
- Preserved stock management through `restock()` and `sell()`.

## Python Concepts

- Encapsulation
- Properties and setters
- Public and non-public attributes
- Attribute validation
- DRY principle

## Result

Product attributes are now managed through controlled interfaces, preventing invalid price and stock updates through normal attribute access.

## Next Step

Explore Inheritance and extend the Product class with specialized product types.
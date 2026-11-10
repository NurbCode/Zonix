# Development Log

This log reflects the code and documentation currently present in the repository.

## Stage 00 — Project Setup

**Status:** Completed

The repository has a basic Python package layout, Git ignore rules, and placeholders for future configuration and dependency files.

## Stage 01 — Python and Object-Oriented Programming

**Status:** Completed

### Catalog model

- Implemented abstract `Product` with name, validated `Decimal` price, and non-negative integer stock.
- Added a writable `price` property and read-only `quantity` property. Stock changes go through `restock()` and `sell()`.
- Added abstract `get_product_info()` and shared `_get_base_product_info()` formatting.
- Implemented `PhysicalProduct` with a positive decimal weight and `DigitalProduct` with positive decimal file size and a non-empty download URL.
- Implemented `Category` composition for grouping products, rejecting duplicate membership, removing products, and returning a shallow copy of the product list.
- Added string and developer representations for product and category objects.
- Added `calculate_total()`, `apply_discount()`, and standalone `is_available()` helpers in `apps/catalog/pricing.py`.

### Automated checks

- The test suite uses Python `unittest` and covers product validation and stock operations, category behavior, and pricing helpers.
- Run it with `python -m unittest discover -s tests -v`.
- Check style with Flake8 using `python -m flake8 apps tests main.py`.
- `main.py` demonstrates concrete physical and digital products, category composition, polymorphism, encapsulation, and object representations.

### Known limitations

- The pricing helpers check selected value constraints but do not consistently validate argument types.
- `Product` calls `name.strip()` without first checking that `name` is a string.
- `Category.products` is publicly mutable; `get_products()` returns a shallow copy, but direct access can still modify membership.
- `DigitalProduct` rejects a blank download URL but does not validate URL syntax.
- Tests cover the pricing helpers; the suite does not provide dedicated tests for every inheritance, polymorphism, and abstract-class behavior.
- `config/` and `requirements/` contain placeholders. Django, Django REST Framework, PostgreSQL, Redis, RabbitMQ, and Docker are planned and are not configured in the repository.

## Planned stages

The README roadmap lists Django fundamentals, persistence, API development, authentication, commerce workflows, caching, background tasks, Docker, and final documentation as future work.

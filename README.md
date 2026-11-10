# Zonix

Zonix is a Python learning project for building an e-commerce backend incrementally. The repository currently contains a small, framework-independent product catalog used to practice Python object-oriented programming. Django and the other backend technologies below are planned, not yet configured.

## Current status

**Stage 01 — Python and object-oriented programming: completed.** The catalog demonstrates inheritance, encapsulation, polymorphism, and abstraction through an abstract `Product` base class and its physical and digital implementations. `Category` demonstrates composition. The project also includes pricing helper functions, 36 automated tests using `unittest`, and PEP 8 style checks with Flake8.

## Repository structure

```text
apps/catalog/
  category.py          Category membership and product collection
  digital_product.py   Digital product implementation
  physical_product.py  Physical product implementation
  pricing.py           Total, discount, and availability helpers
  product.py           Abstract Product base class
docs/
  development-log.md  Project progress summary
  stage-01/            Stage 01 concept notes
main.py                Demonstration script for the catalog and OOP concepts
tests/
  test_category.py     Category behavior tests
  test_products.py     Product validation and stock tests
  test_pricing.py      Pricing helper tests
```

## Implemented functionality

- `Product` validates names, `Decimal` prices, and integer stock quantities. Its price is writable through a validating property; stock is read-only directly and changed through `restock()` and `sell()`.
- `Product` is abstract. `PhysicalProduct` and `DigitalProduct` provide `get_product_info()` implementations and add their own read-only properties.
- `Category` accepts `Product` instances, prevents duplicate membership, supports removal, and returns a shallow copy from `get_products()`.
- `pricing.py` provides `calculate_total()`, `apply_discount()`, and a standalone `is_available()` helper, covered by `tests/test_pricing.py`.
- Product and category objects provide string and developer representations.

## Running the Project

Run the demonstration from the repository root:

```bash
python main.py
```

Run the automated tests:

```bash
python -m unittest discover -s tests -v
```

Check code style with Flake8:

```bash
python -m flake8 apps tests main.py
```

## Roadmap

| Stage | Scope | Status |
|---|---|---|
| 00 | Project setup and Git configuration | Completed |
| 01 | Python OOP (inheritance, encapsulation, polymorphism, abstraction), composition, pricing helpers, 36 unittest cases, and Flake8 | Completed |
| 02 | Django fundamentals | Planned |
| 03 | PostgreSQL and Django ORM | Planned |
| 04 | Django REST Framework | Planned |
| 05 | Authentication and permissions | Planned |
| 06 | E-commerce business logic | Planned |
| 07 | Automated testing | Planned |
| 08 | Redis caching | Planned |
| 09 | RabbitMQ and background tasks | Planned |
| 10 | Docker | Planned |
| 11 | Finalization and documentation | Planned |

## Development approach

Each stage adds a small implementation and documents the concepts and decisions behind it. The roadmap describes future learning goals; only the functionality listed under “Implemented functionality” is present in the repository today.

# Zonix

Zonix is a Python learning project for building an e-commerce backend incrementally. The repository currently contains a small, framework-independent product catalog used to practice Python object-oriented programming. Django and the other backend technologies below are planned, not yet configured.

## Current status

**Stage 01 — Python and object-oriented programming: implemented in source.** The catalog includes an abstract product base class, physical and digital products, categories, stock and price validation, and pricing helpers. No automated test files or dependency manifests have been committed yet. The `config/`, `requirements/`, and `tests/` directories currently contain placeholders only.

`main.py` is an in-progress demonstration script. It currently attempts to instantiate the abstract `Product` class, so it raises `TypeError` before reaching the category demonstration. Instantiate `PhysicalProduct` or `DigitalProduct` to exercise the current hierarchy.

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
main.py                In-progress demonstration script
```

## Implemented functionality

- `Product` validates names, `Decimal` prices, and integer stock quantities. Its price is writable through a validating property; stock is read-only directly and changed through `restock()` and `sell()`.
- `Product` is abstract. `PhysicalProduct` and `DigitalProduct` provide `get_product_info()` implementations and add their own read-only properties.
- `Category` accepts `Product` instances, prevents duplicate membership, supports removal, and returns a shallow copy from `get_products()`.
- `pricing.py` provides `calculate_total()`, `apply_discount()`, and a standalone `is_available()` helper.
- Product and category objects provide string and developer representations.

## Running the current demonstration

The project uses only the Python standard library and has no dependency file yet. Run the script from the repository root with:

```console
python main.py
```

The script needs to be updated to use a concrete product class before it can run successfully; see the current status above.

## Roadmap

| Stage | Scope | Status |
|---|---|---|
| 00 | Project setup and Git configuration | Completed |
| 01 | Python, OOP, and PEP 8 | Completed |
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

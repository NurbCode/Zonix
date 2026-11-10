# Development Log

This file summarizes the implementation currently present in the repository. It does not record a verified test run; automated test files are not checked in.

## Stage 00 — Project Setup

**Status:** Completed

The repository has a basic Python package layout, Git ignore rules, and placeholders for configuration, requirements, and tests.

## Stage 01 — Python and Object-Oriented Programming

**Status:** Core learning implementation present

### Catalog model

- Added abstract `Product` with name, validated `Decimal` price, and non-negative integer stock.
- Added a writable `price` property and read-only `quantity` property. Stock changes go through `restock()` and `sell()`.
- Added abstract `get_product_info()` and shared `_get_base_product_info()` formatting.
- Added `PhysicalProduct` with a positive decimal weight.
- Added `DigitalProduct` with positive decimal file size and a non-empty download URL.
- Added `Category` for grouping concrete products, duplicate rejection, removal, and a shallow-copy accessor.
- Added string and developer representations for products and categories.
- Added pricing helpers in `apps/catalog/pricing.py`: `calculate_total()`, `apply_discount()`, and standalone `is_available()`.

### Documentation

Stage notes cover category composition, encapsulation, inheritance, polymorphism, and abstract classes. The README describes the current source tree and planned roadmap.

### Repository gaps

- `tests/` has no committed tests, despite previous notes naming test files that are absent.
- `requirements/` and `config/` contain placeholders only; Django, Django REST Framework, PostgreSQL, Redis, RabbitMQ, and Docker are not configured here.
- `main.py` currently instantiates the abstract `Product` class, so the demonstration script fails before its later examples execute. It needs concrete product instances to serve as a runnable demo.
- `pricing.py` performs some value checks, but does not consistently validate argument types; its helpers should not be described as fully validated APIs.

## Planned stages

The README roadmap lists Django fundamentals, persistence, API development, authentication, commerce workflows, tests, caching, background tasks, Docker, and final documentation as future work. These are learning goals, not features already present in the codebase.

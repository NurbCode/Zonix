# Inheritance, Polymorphism & Abstract Classes

## 1. Inheritance

Inheritance allows one class to inherit attributes and methods from another class.

In Zonix, `Product` is the parent class, while `PhysicalProduct` and `DigitalProduct` are child classes.

### Product hierarchy

- `Product` — base class.
- `PhysicalProduct` — represents physical products.
- `DigitalProduct` — represents digital products.

### PhysicalProduct

Additional attribute:
- `weight_kg` — product weight in kilograms.

Uses `super().__init__()` to reuse the parent constructor.

### DigitalProduct

Additional attributes:
- `file_size_mb` — digital file size.
- `download_url` — download link.

Both child classes reuse the common product functionality:
- `sell()`
- `restock()`
- `is_available()`
- `price`
- `quantity`

## 2. Polymorphism

Polymorphism allows different classes to implement the same method in different ways.

In Zonix, all product types implement:

`get_product_info()`

Implementations:
- `PhysicalProduct` returns general product information and weight.
- `DigitalProduct` returns general product information, file size and download URL.

The method is overridden in both child classes.

Dynamic dispatch allows Python to select the correct implementation based on the object's actual type.

## 3. Abstract Classes

Abstract classes define a common interface for their subclasses.

The `Product` class inherits from `ABC`:

`class Product(ABC):`

The `@abstractmethod` decorator marks methods that must be implemented by child classes.

Abstract method:

`get_product_info()`

Both `PhysicalProduct` and `DigitalProduct` implement this method.

The abstract `Product` class cannot be instantiated directly.

### Shared product information

The `_get_base_product_info()` method provides common product information:

- Name
- Price
- Stock quantity

Child classes reuse this method to avoid code duplication.

## 4. Project Structure

```text
apps/
└── catalog/
    ├── __init__.py
    ├── product.py
    ├── category.py
    ├── physical_product.py
    ├── digital_product.py
    └── pricing.py
```

## 5. Testing

The following test files were used during development:

- `test_inheritance.py`
- `test_polymorphism.py`
- `test_abstract.py`

The tests cover:

- Creating physical and digital products.
- Inheriting parent class functionality.
- Overriding methods.
- Polymorphic method calls.
- Preventing direct instantiation of the abstract Product class.

## 6. Key Concepts Learned

- Inheritance
- Parent and child classes
- `super()`
- Method overriding
- Polymorphism
- Dynamic dispatch
- Abstract Base Classes (ABC)
- `@abstractmethod`

**Stage 01 progress:** Inheritance, Polymorphism and Abstract Classes implemented.
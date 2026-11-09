
from decimal import Decimal

from apps.catalog.product import Product


class DigitalProduct(Product):
    def __init__(
        self,
        name: str,
        price: Decimal,
        quantity: int,
        file_size_mb: Decimal,
        download_url: str
    ) -> None:
        super().__init__(name, price, quantity)

        if not isinstance(file_size_mb, Decimal):
            raise TypeError("File size must be a Decimal.")

        if file_size_mb <= 0:
            raise ValueError("File size must be positive.")

        if not download_url.strip():
            raise ValueError("Download URL cannot be empty.")

        self._file_size_mb = file_size_mb
        self._download_url = download_url


    @property
    def file_size_mb(self) -> Decimal:
        return self._file_size_mb


    @property
    def download_url(self) -> str:
        return self._download_url


    def __str__(self) -> str:
        return (
            f"{super().__str__()} "
            f"(Digital, {self.file_size_mb} MB)"
        )


    def get_product_info(self) -> str:
        return (
            f"{self._get_base_product_info()}\n"
            f"Type: Digital\n"
            f"File size: {self.file_size_mb} MB\n"
            f"Download URL: {self.download_url}"
        )

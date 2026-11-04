from magazine import utils
from magazine.Product import Product


class Order:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def total(self) -> float:
        return sum(product.price for product in self.products)

    def __str__(self) -> str:
        return (
            f"Zamówienie: {len(self.products)} poz., "
            f"razem {utils.format_price(self.total())}"
        )

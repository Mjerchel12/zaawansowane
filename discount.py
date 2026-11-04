def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 1):
        raise ValueError("discount must be between 0 and 1")
    return price * (1 - discount)
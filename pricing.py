def apply_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid discount")

    return price - (price * discount_percent / 100)

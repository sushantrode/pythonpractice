def get_price(price):
    return price if price > 0 else 0

original_prices = [1.25, 0, 10.22, 3.78, 0, 1.16]
prices = [get_price(i) for i in original_prices]
PRICES = {
    "apple": 1.0,
    "banana": 0.5,
    "cherry": 0.75,
    "mango": 1.0,
    "pineapple": 1.5,
    "dragonfruit": 2.0,
    "durian": 2.75,
}

def calculate_total_price(items):
    total = 0
    for item in items:
        price = PRICES.get(item)
        if price is not None:
            total += price
        else:
            print("Unknown item:", item)

    if total >= 10:
        total *= 0.9  # apply discount

    return total

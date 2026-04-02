"""DealFinder - A simple tool to find and compare deals."""


def find_best_deal(deals):
    """Return the deal with the lowest price from a list of deals.

    Args:
        deals: list of dicts with 'name' and 'price' keys

    Returns:
        The deal dict with the lowest price, or None if the list is empty.
    """
    if not deals:
        return None
    return min(deals, key=lambda d: d["price"])


def filter_deals_by_max_price(deals, max_price):
    """Return deals with a price at or below max_price.

    Args:
        deals: list of dicts with 'name' and 'price' keys
        max_price: maximum price threshold

    Returns:
        Filtered list of deals.
    """
    return [d for d in deals if d["price"] <= max_price]

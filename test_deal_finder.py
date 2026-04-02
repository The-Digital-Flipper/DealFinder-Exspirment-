"""Tests for deal_finder module."""
import unittest

from deal_finder import filter_deals_by_max_price, find_best_deal


class TestFindBestDeal(unittest.TestCase):
    def test_returns_none_for_empty_list(self):
        self.assertIsNone(find_best_deal([]))

    def test_returns_single_deal(self):
        deals = [{"name": "Widget", "price": 9.99}]
        self.assertEqual(find_best_deal(deals), deals[0])

    def test_returns_cheapest_deal(self):
        deals = [
            {"name": "Widget A", "price": 19.99},
            {"name": "Widget B", "price": 9.99},
            {"name": "Widget C", "price": 14.99},
        ]
        self.assertEqual(find_best_deal(deals)["name"], "Widget B")


class TestFilterDealsByMaxPrice(unittest.TestCase):
    def test_returns_empty_for_empty_list(self):
        self.assertEqual(filter_deals_by_max_price([], 10), [])

    def test_filters_above_max_price(self):
        deals = [
            {"name": "Cheap", "price": 5.00},
            {"name": "Expensive", "price": 50.00},
        ]
        result = filter_deals_by_max_price(deals, 10)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Cheap")

    def test_includes_deal_at_exact_max_price(self):
        deals = [{"name": "Exact", "price": 10.00}]
        result = filter_deals_by_max_price(deals, 10)
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()

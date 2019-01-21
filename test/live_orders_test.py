import unittest, sys, os

sys.path.append(os.getcwd())
from src.live_orders import LiveOrders
from src.order import Order


class TestLiveOrders(unittest.TestCase):
    def test_add(self):
        LiveOrders.add("a123", 5, 10, LiveOrders.BUY)

        assert len(LiveOrders.log) == 1

        stored_order = LiveOrders.log[0]

        assert stored_order.user_id == "a123"
        assert stored_order.quantity == 5
        assert stored_order.price_per_kilo == 10
        assert stored_order.type == "BUY"

        LiveOrders.add("b456", 7, 10, LiveOrders.BUY)

        assert len(LiveOrders.log) == 1

        updated_stored_order = LiveOrders.log[0]

        assert stored_order.quantity == 12

        LiveOrders.add("b456", 7, 4, LiveOrders.SELL)

        assert len(LiveOrders.log) == 2

    def test_delete(self):
        order = Order("c789", 2, 3, LiveOrders.BUY)
        LiveOrders.log.append(order)
        LiveOrders.delete(order.object_id)

        assert order not in LiveOrders.log

    def test_list_sorted(self):
        LiveOrders.add("a123", 8, 3, LiveOrders.BUY)
        LiveOrders.add("a123", 5, 6, LiveOrders.SELL)

        result = LiveOrders.list_sorted()
        assert result[0].price_per_kilo == 10
        assert result[1].price_per_kilo == 3
        assert result[2].price_per_kilo == 4
        assert result[3].price_per_kilo == 6


if __name__ == "__main__":
    unittest.main()

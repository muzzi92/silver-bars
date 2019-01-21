from .order import Order


class LiveOrders:

    BUY = "BUY"
    SELL = "SELL"
    log = []

    @classmethod
    def add(cls, user_id, quantity, price, _type):
        for order in cls.log:
            if order.price_per_kilo == price and order.type == _type:
                order.quantity += quantity
                return
        order = Order(user_id, quantity, price, _type)
        cls.log.append(order)

    @classmethod
    def delete(cls, object_id):
        for order in cls.log:
            if order.object_id == object_id:
                order_to_delete = order
        cls.log.remove(order_to_delete)

    @classmethod
    def list_sorted(cls):
        buy_list = []
        sell_list = []
        for order in cls.log:
            buy_list.append(order) if order.type == cls.BUY else sell_list.append(order)
        ranked_buys = sorted(buy_list, key=lambda order: -order.price_per_kilo)
        ranked_sells = sorted(sell_list, key=lambda order: order.price_per_kilo)

        return ranked_buys + ranked_sells

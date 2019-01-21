from order import Order

class LiveOrders:

    log = []

    @classmethod
    def add_new(cls, user_id, quantity, price, _type):
        order = Order(user_id, quantity, price, _type)
        cls.log.append(order)

    @classmethod
    def delete(cls, object_id):
        for order in cls.log:
            if order.object_id == object_id:
                order_to_delete = order
        cls.log.remove(order_to_delete)

import uuid


class Order:
    def __init__(self, user_id, quantity, price, _type):
        self.object_id = uuid.uuid1()
        self.user_id = user_id
        self.quantity = quantity
        self.price_per_kilo = price
        self.type = _type

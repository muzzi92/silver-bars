import os, sys

sys.path.append(os.getcwd())
from src.user import User
from src.live_orders import LiveOrders


class AppEngine:
    @classmethod
    def run(cls):
        user = User(input("Enter username: "))

        selection = None
        while selection != "3":
            cls.display_board()
            print("Choose from the following options: ")
            print("1. Enter new order")
            print("2. Delete an order")
            print("3. Exit application")

            selection = input("Enter a number and hit enter: ")

            if selection == "1":
                cls.entry_form(user.object_id)
            elif selection == "2":
                cls.delete_form()

    @staticmethod
    def entry_form(user_id):
        user_id = user_id
        print("Please enter the following details about your order: ")
        quantity = float(input("Quantity in Kg to one decimal place: "))
        price = int(input("Enter price per kilo to be paid, in whole pounds: "))
        _type = (
            LiveOrders.SELL
            if input("Enter transaction type ('b' for buy/ 's' for sell): ").lower()
            == "b"
            else LiveOrders.BUY
        )

        LiveOrders.add(user_id, quantity, price, _type)

        print("Order added.")

    @staticmethod
    def display_board():
        print("LIVE ORDER BOARD")
        for order in LiveOrders.list_sorted():
            print(f"{'='*40}")
            print(f"{order.type}: {order.quantity}kg for £{order.price_per_kilo}")
            print(f"{'='*40}")

    @staticmethod
    def delete_form():
        order_mappings = {}
        for index, order in enumerate(LiveOrders.list_sorted()):
            number = str(index + 1)
            order_mappings.update({number: order.object_id})
            print(f"{'='*40}")
            print(
                f"{number}: {order.type}: {order.quantity}kg for £{order.price_per_kilo}"
            )
            print(f"{'='*40}")
        print("Which Order would you like to remove?")
        selection = input("Enter a number and hit enter: ")

        LiveOrders.delete(order_mappings[selection])


def main():
    AppEngine.run()


if __name__ == "__main__":
    main()

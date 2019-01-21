from user import User
from live_orders import LiveOrders

class AppEngine:

    def run(self):
        username = input("Enter username: ")
        user = User(username)

        selection = None

        while selection != "4":
            print("Choose from the following options: ")
            print("1. Enter new order")
            print("2. Delete an order")
            print("3. View Live Order Board")
            print("4. Exit application")

            selection = input("Enter a number and hit enter: ")

            if selection == "1":
                self.order_entry(user.object_id)
            elif selection == "2":
                self.delete_form()
            elif selection == "3":
                self.display_board()

    def order_entry(self, user_id):
        user_id = user_id
        print("Please enter the following details about your order: ")
        quantity = float(input("Quantity in Kg to one decimal place: "))
        price = int(input("Enter price per kilo to be paid, in whole pounds: "))
        _type = input("Enter transaction type (buy/sell): ")

        LiveOrders.add_new(user_id, quantity, price, _type)

        print("Order added.")

    def display_board(self):
        print("LIVE ORDER BOARD")
        for order in LiveOrders.log:
            print(f"{'='*40}")
            print(f"{order.type}: {order.quantity}kg for £{order.price_per_kilo}")
            print(f"{'='*40}")

    def delete_form(self):
        order_id_to_delete = None
        order_mappings = []
        for index, order in enumerate(LiveOrders.log):
            number = index + 1
            order_mappings.append({"number": number, "order_id": order.object_id})
            print(f"{'='*40}")
            print(f"{number}: {order.type}: {order.quantity}kg for £{order.price_per_kilo}")
            print(f"{'='*40}")
        print("Which Order would you like to remove?")
        selection = int(input("Enter a number and hit enter: "))
        for order in order_mappings:
            if order["number"] == selection:
                LiveOrders.delete(order["order_id"])


def main():
    AppEngine().run()


if __name__ == "__main__":
    main()

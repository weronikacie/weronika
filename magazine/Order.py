from magazine import utils

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        print(f"Zamówienie nr: {self.order_id}")
        print(utils.helper_function())
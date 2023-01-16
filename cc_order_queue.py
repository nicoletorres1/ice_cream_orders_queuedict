class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor in self.flavors:
            if scoops >= 1 and scoops <= 3:
                print('order created!')
            else:
                print("Sorry, we don't have that flavor.\nChoose between 1-3 scoops")
        order = {"Customer": customer, "Flavor": flavor, "Scoops": scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        print("All pendinig ice cream orders\n")
        for order in self.orders.items:
            # print(self.orders.items)
            print(
                f"Customer: {order['Customer']}- - Flavor: {order['Flavor']} - - Scoops: {order['Scoops']}")

    def next_order(self):
        # if not empty
        if self.orders:
            next_order = self.orders.dequeue()
            print("next order up!")
            print(
                f"{next_order['Customer']}, {next_order['Flavor']}, {next_order['Scoops']}")
        else:
            print("No more orders in queue.")


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()

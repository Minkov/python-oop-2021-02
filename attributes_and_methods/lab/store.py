class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items_count = 0
        self.items = {}

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'

    # V1
    # @staticmethod
    # def can_add_item(items, capacity):
    #     total_items_count = sum(value for value in items.values())
    #     return total_items_count == capacity

    @staticmethod
    def can_add_item(count, capacity):
        return count < capacity

    @staticmethod
    def can_remove_item(items, item_name, amount):
        return item_name in items \
               and amount <= items[item_name]

    @classmethod
    def from_size(cls, name, type, size):
        return cls(name, type, size // 2)

    def add_item(self, item):
        # V1
        # if not self.can_add_item(self.items, self.capacity):
        #     return 'Not enough capacity in the store'

        # V2
        if not self.can_add_item(self.items_count, self.capacity):
            return 'Not enough capacity in the store'
        self.items_count += 1

        if item not in self.items:
            self.items[item] = 0
        self.items[item] += 1
        return f'{item} added to the store'

    def remove_item(self, item, amount):
        if not self.can_remove_item(self.items, item, amount):
            return f'Cannot remove {amount} {item}'

        self.items_count -= amount
        self.items[item] -= amount
        return f'{amount} {item} removed from the store'


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))

print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.values_count = 0

    def append(self, value):
        node = LinkedListNode(value)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.values_count += 1
        return self

    def remove(self, index):
        node = self.__get_node(index)
        node.prev.next = node.next
        node.next.prev = node.prev
        self.values_count -= 1
        return node.value

    def get(self, index):
        node = self.__get_node(index)
        return node.value

    def extend(self, iterable):
        self.__validate_iterable(iterable)
        [self.append(x) for x in iterable]

    def pop(self):
        self.__validate_index(0)
        node = self.tail

        node.prev.next = None
        self.tail = node.prev
        self.values_count -= 1

        return node.value

    def clear(self):
        self.head = None
        self.tail = None
        self.values_count = 0

    def index(self, value):
        node = self.head
        index = 0
        while node:
            if node.value == value:
                return index
            node = node.next
            index += 1

        raise ValueError

    def add_first(self, value):
        node = LinkedListNode(value)
        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.values_count += 1

    def size(self):
        return self.values_count

    def copy(self):
        copied_list = LinkedList()
        [copied_list.append(x) for x in self]
        return copied_list

    def count(self, value):
        node = self.head
        count = 0
        while node:
            if node.value == value:
                count += 1
            node = node.next
        return count

    def insert(self, index, value):
        node = self.__get_node(index)
        new_node = LinkedListNode(value)

        node.prev.next = new_node
        new_node.prev = node.prev

        node.prev = new_node
        new_node.next = node

    def __get_node(self, index):
        self.__validate_index(index)
        i = 0
        node = self.head
        while node and i < index:
            node = node.next
            i += 1
        return node

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    @staticmethod
    def __validate_iterable(iterable):
        if not getattr(iterable, '__iter__', False):
            raise ValueError

    def __validate_index(self, index):
        if self.values_count <= index:
            raise IndexError

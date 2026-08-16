class Node:
    def __init__(self, key, val, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = pre
        self.next = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.mlength = capacity
        self.cache = {}
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Already the most recently used
        if node == self.tail:
            return node.val

        # Remove from current position
        if node == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            prev, nxt = node.prev, node.next
            if prev:
                prev.next = nxt
            if nxt:
                nxt.prev = prev

        # Move to tail
        node.prev = self.tail
        node.next = None
        if self.tail:
            self.tail.next = node
        self.tail = node

        return node.val

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            # Already MRU
            if node == self.tail:
                return

            # Remove from current position
            if node == self.head:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
            else:
                prev, nxt = node.prev, node.next
                if prev:
                    prev.next = nxt
                if nxt:
                    nxt.prev = prev

            # Move to tail
            node.prev = self.tail
            node.next = None
            if self.tail:
                self.tail.next = node
            self.tail = node
            return

        # Remove LRU if cache is full
        if self.length >= self.mlength:
            old = self.head
            del self.cache[old.key]

            self.head = old.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

            self.length -= 1

        # Insert new node
        n = Node(key, value)

        if self.tail:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        else:
            self.head = n
            self.tail = n

        self.cache[key] = n
        self.length += 1
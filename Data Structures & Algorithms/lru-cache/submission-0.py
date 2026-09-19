# double linked list class
class ListNode:
    def __init__(self, key = None, val: int = 0, next: ListNode | None = None, prev: ListNode | None = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # dict: key -> corresp ListNode
        self.cache: dict[int, ListNode] = {}
        self.capacity = capacity 
        # dummy nodes
        self.head = ListNode() # head: most recently used
        self.tail = ListNode() # tail: least recently used

        self.head.prev = self.head.next = self.tail
        self.tail.prev = self.tail.next = self.head

    def _remove(self, node: ListNode) -> None:
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def _insert_front(self, node: ListNode) -> None:
        self.head.next.prev = node
        node.next = self.head.next

        node.prev = self.head
        self.head.next = node

    def get(self, key: int) -> int: 
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = ListNode(key = key, val = value)
            self._insert_front(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                tmp = self.tail.prev
                self._remove(tmp)
                del self.cache[tmp.key]
        else:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._insert_front(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
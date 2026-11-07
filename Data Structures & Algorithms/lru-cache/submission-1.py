# need to define a double ll node
class Node:
    def __init__(self, val = 0, key = 0, prev = None, next = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next 

class LRUCache:

    def __init__(self, capacity: int):
        self.maxCap = capacity
        self.cap = 0
        self.d = {}
        # dummy sentinel nodes for start and end of the priority queue
        self.dummyStart = Node()
        self.dummyEnd = Node(prev = self.dummyStart)
        self.dummyStart.next = self.dummyEnd

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        node = self.d[key]

        # remove from its position
        node.prev.next = node.next
        node.next.prev = node.prev

        # insert at the beginning: most recently used
        node.prev = self.dummyStart
        node.next = self.dummyStart.next
        self.dummyStart.next.prev = node
        self.dummyStart.next = node

        return node.val

    def put(self, key: int, value: int) -> None:
        # put: insert into dict
        node = Node()
        if key in self.d:
            node = self.d[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node.val = value
            node.key = key
            self.d[key] = node
            self.cap += 1

        # remove node at the end
        if self.cap > self.maxCap:
            del self.d[self.dummyEnd.prev.key]
            self.dummyEnd.prev.prev.next = self.dummyEnd
            self.dummyEnd.prev = self.dummyEnd.prev.prev
            self.cap -= 1
        
        # move to most recent
        node.prev = self.dummyStart
        node.next = self.dummyStart.next
        self.dummyStart.next.prev = node
        self.dummyStart.next = node
    
    # also need keep track of order each key is used
    # priority queue: finding most recent is O(1): first element in the queue
    # if we use a list, moving an itme to the front is not O(1)
    # idea: use double linked list instead. the dict will point to corresp. node, so access is still O(1)


    
        

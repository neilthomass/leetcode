# Last updated: 9/17/2025, 6:08:36 PM
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = Node(-1)  # sentinel head
        self.tail = Node(-1)  # sentinel tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.pos = {}
        self.l = 0

    def add(self, val):
        node = Node(val)
        prev, nxt = self.head, self.head.next
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node
        self.pos[val] = node
        self.l += 1

    def remove(self, val):
        if val not in self.pos:
            return
        node = self.pos[val]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.pos[val]
        self.l -= 1

    def removeLast(self):
        if self.l == 0:
            return None
        node = self.tail.prev
        self.remove(node.val)
        return node.val

    def len(self):
        return self.l

        



class LRUCache:




    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.dll = DLL()

        

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self.dll.remove(key)
        self.dll.add(key)
        return self.d[key]
        

    def put(self, key: int, value: int) -> None:
        self.dll.remove(key)
        self.dll.add(key)
        self.d[key] = value
        if self.dll.len() > self.cap:
            del self.d[self.dll.removeLast()]

            


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
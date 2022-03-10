class _DoublyLinkedBase:    
    
    class _Node:
        __slots__ = '_element', '_prev', '_next'
        
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
            
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element
    
def split(head):
    slow = head
    fast = head._next
 
    while fast:
        fast = fast._next
        if fast:
            slow = slow._next
            fast = fast._next
    return slow

def d_merge(a, b):

    if a is None:
        return b
 
    if b is None:
        return a
 
    if a._element <= b._element:
        a._next = d_merge(a._next, b)
        a._next._prev = a
        a._prev = None
        return a
    else:
        b._next = d_merge(a, b._next)
        b._next._prev = b
        b._prev = None
        return b

def d_mergesort(head):

    if head is None or head._next is None:
        return head
 
    a = head
 
    slow = split(head)
    b = slow._next
    slow._next = None
 
    a = d_mergesort(a)
    b = d_mergesort(b)
 
    head = d_merge(a, b)
    return head
    
if __name__ == '__main__':
 
    keys = [6, 4, 8]
    d = _DoublyLinkedBase()
    head = None
    for key in keys:
        d._insert_between(key, d._header, d._header._next)
    head = d_mergesort(d._header._next)
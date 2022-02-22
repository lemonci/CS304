"""Single list algorithms"""

# Algorithm add_first(L, e):
#     newest = Node(e)         {create new node instance stroing reference to element e}
#     newest.next = L.head     {set new node's next to reference the old head node}
#     L.head = newest          {set variable head to reference the new node}
#     L.size = L.size + 1      {increment the node count}

# Algorithm add_lst(L, e):
    # newest = Node(e)         {create new node instance stroing reference to element e}
    # newest.next = None       {set new node's next to reference the None object}
    # L.tail.next = newest     {make old tail node point to new node}
    # L.tail = newest          {set variable tail to reference the new node}
    # L.size = L.size + 1      {increment the node count}
    
# Algorithem remove_first(K):
    # if L.head is None then:
    #     Indicate an error: the list is empty
    # L.head = L.head.next     {make head point to next node (or None)}
    # L.size = L.size - 1      {decrement the node count}

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass
    
class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    #----------------------- nested _Node class ---------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slot__ = '_element', '_next'        # streamline memory usage
        
        def __init__(self, element, next):    # initialize node's fields
            self._element = element           # reference to user's element
            self._next = next                 # reference to next node
    #---------------------------- stack methods ---------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head = None                     # reference to the head node
        self._size = 0                        # number of stack elements
        
    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0
    
    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head) # create and link a new node
        self._size += 1
        
    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element           # top of stack is at head of list
    
    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e. LIFO).
        
        Raise Empty exception if the stack is empty.
        """
        if self._is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next        # bypass the former top node
        self._size -= 1
        return answer
    
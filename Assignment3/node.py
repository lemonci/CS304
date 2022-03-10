# A Doubly Linked List Node
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
 
 
# Utility function to push a node at the beginning of the doubly linked list
def push(head, key):
 
    node = Node(key, head)
 
    # change `prev` of the existing head node to point to the new node
    if head:
        head.prev = node
 
    # return new head node
    return node
 
 
# Helper function to print nodes of a doubly linked list
def printDDL(head):
 
    while head:
        print(head.data, end=' ⇔ ')
        head = head.next
    print('None')
 
 
# Function to split nodes of the given doubly linked list into
# two halves using the fast/slow pointer strategy
def split(head):
 
    slow = head
    fast = head.next
 
    # advance `fast` by two nodes, and advance `slow` by a single node
    while fast:
        fast = fast.next
        if fast:
            slow = slow.next
            fast = fast.next
 
    return slow
 
 
# Recursive function to merge nodes of two sorted lists
# into a single sorted list
def merge(a, b):
 
    # base cases
    if a is None:
        return b
 
    if b is None:
        return a
 
    # pick either `a` or `b`, and recur
    if a.data <= b.data:
        a.next = merge(a.next, b)
        a.next.prev = a
        a.prev = None
        return a
    else:
        b.next = merge(a, b.next)
        b.next.prev = b
        b.prev = None
        return b
 
 
# Function to sort a doubly-linked list using merge sort algorithm
def mergesort(head):
 
    # base case: 0 or 1 node
    if head is None or head.next is None:
        return head
 
    # split head into `a` and `b` sublists
    a = head
 
    slow = split(head)
    b = slow.next
    slow.next = None
 
    # recursively sort the sublists
    a = mergesort(a)
    b = mergesort(b)
 
    # merge the two sorted lists
    head = merge(a, b)
    return head
 
 
if __name__ == '__main__':
 
    keys = [6, 4, 8]
 
    head = None
    for key in keys:
        head = push(head, key)
 
    head = mergesort(head)
    printDDL(head)
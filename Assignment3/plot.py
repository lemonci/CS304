import time
import numpy as np
import matplotlib.pyplot as plt


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
def mergesort_d(head):
 
    # base case: 0 or 1 node
    if head is None or head.next is None:
        return head
 
    # split head into `a` and `b` sublists
    a = head
 
    slow = split(head)
    b = slow.next
    slow.next = None
 
    # recursively sort the sublists
    a = mergesort_d(a)
    b = mergesort_d(b)
 
    # merge the two sorted lists
    head = merge(a, b)
    return head


def merge_a(A,p,q,r):  
    n1 = q - p + 1
    n2 = r - q
   # print("\nmerging, p="+str(p)+' q='+str(q)+" r="+str(r)+" n1="+str(n1)+" n2="+str(n2) + ", arr[p:r]="+str(arr[p:r+1]))
    L = []
    R = []
    for i in range(n1):
        L.append(A[p+i])
    for i in range(n2):
        R.append(A[q+i+1])
    L.append(99999)
    R.append(99999)  
   # print('L = ' + str(L) + " R = " + str(R))
    
    i=0
    j=0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1 
    #print("MERGED = " + str(A)+"\n")
    
def mergesort(A,p,r):
   # if p<r:
       # print('p<r? True. p = ' + str(p) +" r = " + str(r))
   # else:
       # print('p<r? False. p = ' + str(p) +" r = " + str(r) +", RETURNING...")
    if p < r:
        q = (p + r) // 2
       # print("calling merge_sort (left half) with p=" + str(p) + ' r='+str(q))
        mergesort(A,p,q)
       # print("calling merge_sort(right half) with p="+str(q+1)+' r='+str(r))
        mergesort(A,q+1,r)
        merge_a(A,p,q,r)
        
 
if __name__ == '__main__':
    
    times = []
    times2 = []
 
    for i in range(10,1000,10):
        #quicksort(np.arange(0,i),0,i-1)
        keys = np.random.randint(0, 1000, i)
        #print(len(keys))
        head = None
        for key in keys:
            head = push(head, key)
        start_t = time.time()
        head = mergesort_d(head)
        times.append(time.time() - start_t)
        #plt.plot(times)
        start_t = time.time()
        mergesort(keys,0,i-1)
        times2.append(time.time() - start_t)
    
    #x_ticks = range(10,2600,200)
    #plt.xticks(x_ticks)
    plt.plot(times, label="doubly-linked list")
    plt.plot(times2, label="array")
    plt.legend()
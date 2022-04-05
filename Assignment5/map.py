import random
from random import shuffle 
#1) BST (binary search tree)
class BST:
    def __init__(self, pair = None):
        self.left = None
        self.right = None
        self.pair = pair
        
    def insert(self, pair):
        if not self.pair:
            self.pair = pair
            return
        if self.pair[0] == pair[0]:
            return
        if pair[0] < self.pair[0]:
            if self.left:
                self.left.insert(pair)
                return
            self.left = BST(pair)
            return
        if self.right:
            self.right.insert(pair)
            return
        self.right = BST(pair)
        
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.pair[0]
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.pair[0]
    def __delitem__(self, key):
        if self == None:
            return self
        if key < self.pair[0]:
            self.left = self.left.__delitem__(key)
            return self
        if key > self.pair[0]:
            self.right = self.right.__delitem__(key)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node:
            min_larger_node = min_larger_node.left
        self.pair = min_larger_node.pair
        self.right = self.right.__delitem__(min_larger_node.key)
        return self
    def exists(self, key):
        if key == self.pair[0]:
            return True
        if key < self.pair[0]:
            if self.left == None:
                return False
            return self.left.exists(key)
        if self.right == None:
            return False
        return self.right.exists(key)
    def __len__(self):
        size = 0
        if self.pair != None:
            size += 1
            if self.left != None:
                size += self.left.__len__()
            if self.right != None:
                size += self.right.__len__()
        return size
    
    def __getitem__(self, key):
        if key == self.pair[0]:
            return self.pair[1]
        if key < self.pair[0]:
            if self.left == None:
                raise KeyError("%s is not in the tree." % key)
            return self.left.__getitem__(key)
        if self.right == None:
            raise KeyError("%s is not in the tree." % key)
        return self.right.__getitem__(key)
        
    def __setitem__(self, key, val):
        pair_n = (key, val)
        if key == self.pair[0]:
            self.pair = pair_n
            return
        if key < self.pair[0]:
            if self.left == None:
                raise KeyError("%s is not in the tree." % key)
            self.left.__setitem__(key, val)
        if self.right == None:
            raise KeyError("%s is not in the tree." % key)
        self.right.__setitem__(key, val)

# HashMapBase


class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic Item class."""
#------------------------------- nested Item class -------------------------------
    class Item:
    """Lightweight composite to store key-value pairs as map items."""
        slots = _key , _value
        def init (self, k, v):
            self. key = k
            self. value = v       
        def eq (self, other):
            return self. key == other. key # compare items based on their keys
        def ne (self, other):
            return not (self == other) # opposite of eq
        def lt (self, other):
            return self. key < other. key # compare items based on their keys

class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""
    def __init__(self, cap=11, p = 109345121):
        """Create an empty hash-table map."""
        self._table = cap * [None]
        self._n = 0                         # number of entries in the map
        self._prime = p                     # prime for MAD compression
        self._sacle = 1 + randrange(p-1)    # scale from 1 to p-1 for MAD
        self._shift = randrange(p)          # shift from 0 to p-1 for MAD

    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)
    
    def __len__(self):
        return self._n
    
    def __getiem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)   # may raise KeyError

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)               # subroutine maintains self._n
        if self._n > len(self._table) // 2:         # keep load factor <= 0.5
            self._resize(2 * len(self._table)-1)    # number 2^x - 1 is often prime
            
    def __delitem__(self, k):
29 j = self. hash function(k)
30 self. bucket delitem(j, k) # may raise KeyError
31 self. n −= 1
32
33 def resize(self, c): # resize bucket array to capacity c
34 old = list(self.items( )) # use iteration to record existing items
35 self. table = c [None] # then reset table to desired capacity
36 self. n = 0 # n recomputed during subsequent adds
37 for (k,v) in old:
38 self[k] = v # reinsert old key-value pair
    
LEN = 10
keys = list(range(LEN))
shuffle(keys)


dic = []
for key in keys:
    dic.append((key, random.random()))

# ===========================insertion for BST==============================
# tree = BST()
# for item in dic:
#     tree.insert(item)
# =============================================================================

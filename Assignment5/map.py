import random
from random import shuffle, randrange
from collections.abc import MutableMapping

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
    class _Item:
        """Lightweight composite to store key-value pairs as map items."""
        __slots__ = '_key', '_value'
        def __init__(self, k, v):
            self._key = k
            self._value = v       
        def __eq__(self, other):
            return self._key == other._key # compare items based on their keys
        def __ne__(self, other):
            return not (self == other) # opposite of __eq__
        def __lt__(self, other):
            return self._key < other._key # compare items based on their keys

class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""
    def __init__(self):
        """Create an empty map."""
        self._table = []
        
    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key:                  # Found a match:
                item._value = v                 # reassign value
                return                          # and quit
           # did not find match for key
        self._table.append(self._Item(k,v))
        
    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if k == self._table[j]._key:       # Found a match
                self._table.pop(j)             # remove item
                return                         # and quit
        raise KeyError('Key Error: ' + repr(k))
        
    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)
        
    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key                   # yield the KEY

class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""
    def __init__(self, cap=11, p = 109345121):
        """Create an empty hash-table map."""
        self._table = cap * [None]
        self._n = 0                         # number of entries in the map
        self._prime = p                     # prime for MAD compression
        self._scale = 1 + randrange(p-1)    # scale from 1 to p-1 for MAD
        self._shift = randrange(p)          # shift from 0 to p-1 for MAD

    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)
    
    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)   # may raise KeyError

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)               # subroutine maintains self._n
        if self._n > len(self._table) // 2:         # keep load factor <= 0.5
            self._resize(2 * len(self._table)-1)    # number 2^x - 1 is often prime
            
    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k) # may raise KeyError
        self._n -= 1
        
    def _resize(self, c): # resize bucket array to capacity c
        old = list(self.items( )) # use iteration to record existing items
        self._table = c * [None] # then reset table to desired capacity
        self._n = 0 # n recomputed during subsequent adds
        for (k,v) in old:
            self[k] = v # reinsert old key-value pair

# 2) Hash table (separate chaining)
class ChainHashMap(HashMapBase):
    # Hash map implemented with separate chaining for collision resolution.
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError( 'Key Error: '+ repr(k)) # no match found
        return bucket[k] # may raise KeyError
        
    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap( ) # bucket is new to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize: # key was new to the table
            self._n += 1 # increase overall map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: '+ repr(k)) # no match found
        del bucket[k] # may raise KeyError

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None: # a nonempty slot
                for key in bucket:
                    yield key

# 3) Hash table (linear probing)
class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""
    _AVAIL = object()   # sentinal marks locations of previous deletions
    
    def _is_available(self, j):
        """Return True if index j is available in table."""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL
    
    def _find_slot(self, j, k):
        """Search for key k in bucket at index j.
        
        Return (success, index) tuple, described as follows:
        if match was found, success is True and index denotes its location.
        if no match found, success is False and index denotes first available slot.
        """
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j          # mark this as first available
                if self._table[j] is None:
                    return (False, firstAvail) # search has failed
            elif k == self._table[j]._key:
                return (True, j)                # found a match
            j = ( j + 1 ) % len (self._table)   # keep looking (cyclically)
            
    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k)) # no match found
        return self._table[s]._value
        
    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)   # insert new item
            self._n += 1                        # size has increased
        else:
            self._table[s]._vale = v            # overwrite existing
            
    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k)) # no match found
        self._table[s] = ProbeHashMap._AVAIL        # mark as vacated

    def __iter__(self):     # scan entire table
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key
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
c = ChainHashMap()
for item in dic:
    c[item[0]] = item[1]

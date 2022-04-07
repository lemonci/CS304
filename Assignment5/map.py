import math, os, time
from random import shuffle, randrange, random, Random
from collections.abc import MutableMapping
from matplotlib import pyplot as plt
import numpy as np

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
            raise KeyError("The key has already in the tree.")
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
        while min_larger_node.left != None:
            min_larger_node = min_larger_node.left
        self.pair = min_larger_node.pair
        self.right = self.right.__delitem__(min_larger_node.pair[0])
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
        if !self.exists(key):
            self.insert(pair_n)
        else:
            if key == self.pair[0]:
                self.pair = pair_n
                return
            if key < self.pair[0]:
                if self.left.pair == None:
                    raise KeyError("%s is not in the tree." % key)
                self.left.__setitem__(key, val)
            if self.right.pair == None:
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
            self._table[s]._value = v            # overwrite existing
            
    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k)) # no match found
        self._table[s] = ProbeHashMap._AVAIL        # mark as vacated

    def __iter__(self):     # scan entire table
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key

# 4) Skip list
class SkipList(object):
    """An indexable skip list.
    A SkipList provides an ordered sequence of key-value pairs. The list is
    always sorted on key and supports O(1) forward iteration. It has O(log N)
    time complexity for key lookup, pair insertion and pair removal anywhere in
    the list. The list also supports O(log N) element access by position.
    The keys of all pairs you add to the skiplist must be be comparable against
    each other, and define the ``<`` and ``<=`` operators.
    """

    UNSET = object()

    p = int((1<<31) / math.e)
    maxlevel = 20

    _rnd = Random()
    _rnd.seed(os.urandom(16))

    __slots__ = ('_level', '_head', '_tail', '_path', '_distance')

    def __init__(self):
        self._level = 1
        self._head = self._new_node(self.maxlevel, None, None)
        self._tail = self._new_node(self.maxlevel, None, None)
        for i in range(self.maxlevel):
            self._head[2+i] = self._tail
        self._path = [None] * self.maxlevel
        self._distance = [None] * self.maxlevel

    def _new_node(self, level, key, value):
        # Node layout: [key, value, next*LEVEL, skip?]
        # The "skip" element indicates how many nodes are skipped by the
        # highest level incoming link.
        if level == 1:
            return [key, value, None]
        else:
            return [key, value] + [None]*level + [0]

    def _random_level(self):
        # Exponential distribution as per Pugh's paper.
        l = 1
        maxlevel = min(self.maxlevel, self.level+1)
        while l < maxlevel and self._rnd.getrandbits(31) < self.p:
            l += 1
        return l

    def _create_node(self, key, value):
        # Create a new node, updating the list level if required.
        level = self._random_level()
        if level > self.level:
            self._tail[-1] = len(self)
            self._level = level
            self._path[level-1] = self._head
            self._distance[level-1] = 0
        return self._new_node(level, key, value)

    def _find_lt(self, key):
        # Find path to last node < key
        node = self._head
        distance = 0
        for i in reversed(range(self.level)):
            nnode = node[2+i]
            while nnode is not self._tail and nnode[0] < key:
                nnode, node = nnode[2+i], nnode
                distance += 1 if i == 0 else node[-1]
            self._path[i] = node
            self._distance[i] = distance

    def _find_lte(self, key):
        # Find path to last node <= key
        node = self._head
        distance = 0
        for i in reversed(range(self.level)):
            nnode = node[2+i]
            while nnode is not self._tail and nnode[0] <= key:
                nnode, node = nnode[2+i], nnode
                distance += 1 if i == 0 else node[-1]
            self._path[i] = node
            self._distance[i] = distance

    def _find_pos(self, pos):
        # Create path to node at pos.
        node = self._head
        distance = 0
        for i in reversed(range(self.level)):
            nnode = node[2+i]
            ndistance = distance + (1 if i == 0 else nnode[-1])
            while nnode is not self._tail and ndistance <= pos:
                nnode, node, distance = nnode[2+i], nnode, ndistance
                ndistance += 1 if i == 0 else nnode[-1]
            self._path[i] = node
            self._distance[i] = distance

    def _insert(self, node):
        # Insert a node in the list. The _path and _distance must be set.
        path, distance = self._path, self._distance
        # Update pointers
        level = max(1, len(node) - 3)
        for i in range(level):
            node[2+i] = path[i][2+i]
            path[i][2+i] = node
        if level > 1:
            node[-1] = 1 + distance[0] - distance[level-1]
        # Update skip counts
        node = node[2]
        i = 2; j = min(len(node) - 3, self.level)
        while i <= self.level:
            while j < i:
                node = node[i]
                j = min(len(node) - 3, self.level)
            node[-1] -= distance[0] - distance[j-1] if j <= level else -1
            i = j+1

    def _remove(self, node):
        # Remove a node. The _path and _distance must be set.
        path, distance = self._path, self._distance
        level = max(1, len(node) - 3)
        for i in range(level):
            path[i][2+i] = node[2+i]
        # Update skip counts
        value = node[1]
        node = node[2]
        i = 2; j = min(len(node) - 3, self.level)
        while i <= self.level:
            while j < i:
                node = node[i]
                j = min(len(node) - 3, self.level)
            node[-1] += distance[0] - distance[j-1] if j <= level else -1
            i = j+1
        # Reduce level if last node on current level was removed
        while self.level > 1 and self._head[1+self.level] is self._tail:
            self._level -= 1
            self._tail[-1] += self._tail[-1] - len(self)
        return value

    # PUBLIC API ...

    @property
    def level(self):
        """The current level of the skip list."""
        return self._level

    def insert(self, key, value):
        """Insert a key-value pair in the list.
        The pair is inserted at the correct location so that the list remains
        sorted on *key*. If a pair with the same key is already in the list,
        then the pair is appended after all other pairs with that key.
        """
        self._find_lte(key)
        node = self._create_node(key, value)
        self._insert(node)

    def __setitem__(self, key, value):
        """Replace the value of the first key-value pair with key *key*.
        If the key was not found, the pair is inserted.
        """
        self._find_lt(key)
        node = self._path[0][2]
        if node is self._tail or key < node[0]:
            node = self._create_node(key, value)
            self._insert(node)
        else:
            node[1] = value

    def clear(self):
        """Remove all key-value pairs."""
        for i in range(self.maxlevel):
            self._head[2+i] = self._tail
            self._tail[-1] = 0
        self._level = 1

    def __len__(self):
        """Return the number of pairs in the list."""
        dist = 0
        idx = self.level + 1
        node = self._head[idx]
        while node is not self._tail:
            dist += node[-1] if idx > 2 else 1
            node = node[idx]
        dist += node[-1]
        return dist

    __bool__ = __nonzero__ = lambda self: len(self) > 0

    def __repr__(self):
        return type(self).__name__ + '((' + repr(list(self.items()))[1:-1] + '))'

    def items(self, start=None, stop=None):
        """Return an iterator yielding pairs.
        If *start* is specified, iteration starts at the first pair with a key
        that is larger than or equal to *start*. If not specified, iteration
        starts at the first pair in the list.
        If *stop* is specified, iteration stops at the last pair that is
        smaller than *stop*. If not specified, iteration end with the last pair
        in the list.
        """
        if start is None:
            node = self._head[2]
        else:
            self._find_lt(start)
            node = self._path[0][2]
        while node is not self._tail and (stop is None or node[0] < stop):
            yield (node[0], node[1])
            node = node[2]

    __iter__ = items

    def keys(self, start=None, stop=None):
        """Like :meth:`items` but returns only the keys."""
        return (item[0] for item in self.items(start, stop))

    def values(self, start=None, stop=None):
        """Like :meth:`items` but returns only the values."""
        return (item[1] for item in self.items(start, stop))

    def popitem(self):
        """Removes the first key-value pair and return it.
        This method raises a ``KeyError`` if the list is empty.
        """
        node = self._head[2]
        if node is self._tail:
            raise KeyError('list is empty')
        self._find_lt(node[0])
        self._remove(node)
        return (node[0], node[1])

    # BY KEY API ...

    def __getitem__(self, key, default=None):
        """Find the first key-value pair with key *key* and return its value.
        If the key was not found, return *default*. If no default was provided,
        return ``None``. This method never raises a ``KeyError``.
        """
        self._find_lt(key)
        node = self._path[0][2]
        if node is self._tail or key < node[0]:
            return default
        return node[1]

    def __delitem__(self, key):
        """Remove the first key-value pair with key *key*.
        If the key was not found, a ``KeyError`` is raised.
        """
        self._find_lt(key)
        node = self._path[0][2]
        if node is self._tail or key < node[0]:
            raise KeyError('{!r} is not in list'.format(key))
        self._remove(node)

    def pop(self, key, default=UNSET):
        """Remove the first key-value pair with key *key*.
        If a pair was removed, return its value. Otherwise if *default* was
        provided, return *default*. Otherwise a ``KeyError`` is raised.
        """
        self._find_lt(key)
        node = self._path[0][2]
        if node is self._tail or key < node[0]:
            if default is self.UNSET:
                raise KeyError('key {!r} not in list')
            return default
        self._remove(node)
        return node[1]

    def __contains__(self, key):
        """Return whether *key* is contained in the list."""
        self._find_lt(key)
        node = self._path[0][2]
        return node is not self._tail and not key < node[0]

    def index(self, key, default=UNSET):
        """Find the first key-value pair with key *key* and return its position.
        If the key is not found, return *default*. If default was not provided,
        raise a ``KeyError``
        """
        self._find_lt(key)
        node = self._path[0][2]
        if node is self._tail or key < node[0]:
            if default is self.UNSET:
                raise KeyError('key {!r} not in list'.format(key))
            return default
        return self._distance[0]

    def count(self, key):
        """Return the number of pairs with key *key*."""
        count = 0
        pos = self.index(key, -1)
        if pos == -1:
            return count
        count += 1
        for i in range(pos+1, len(self)):
            if self[i][0] != key:
                break
            count += 1
        return count        

tree = BST()
c = ChainHashMap()
p = ProbeHashMap()
s = SkipList()

LEN = 10000
keys = list(range(LEN))
shuffle(keys)
t_tree = [None] * LEN
t_c = [None] * LEN
t_p = [None] * LEN
t_s = [None] * LEN

dic = []
for key in keys:
    dic.append((key, random()))

# ============================== Insert ==============================

for i in range(LEN):
# ============================== BST =================================
    t = time.process_time()
    tree[dic[i][0]] = dic[i][1]
    t = time.process_time() - t
    t_tree[i] = t
# =========================== Hash Table (Chain)======================
    t = time.process_time()
    c[dic[i][0]] = dic[i][1]
    t = time.process_time() - t
    t_c[i] = t
# =========================== Hash Table (Chain)======================
    t = time.process_time()
    p[dic[i][0]] = dic[i][1]
    t = time.process_time() - t
    t_p[i] = t
# =========================== Skip List ==============================
    t = time.process_time()
    s[dic[i][0]] = dic[i][1]
    t = time.process_time() - t
    t_s[i] = t
# ====================================================================


# # =========================== Insert & Visit =========================

for i in range(LEN):
# ============================== BST =================================
    t = time.process_time()
    tree[dic[i][0]] = dic[i][1]
    v = tree[dic[i][0]]
    t = time.process_time() - t
    t_tree[i] = t
# =========================== Hash Table (Chain)======================
    t = time.process_time()
    c[dic[i][0]] = dic[i][1]
    v = c[dic[i][0]]
    t = time.process_time() - t
    t_c[i] = t
# =========================== Hash Table (Chain)======================
    t = time.process_time()
    p[dic[i][0]] = dic[i][1]
    v = p[dic[i][0]]
    t = time.process_time() - t
    t_p[i] = t
# =========================== Skip List ==============================
    t = time.process_time()
    s[dic[i][0]] = dic[i][1]
    v = s[dic[i][0]]
    t = time.process_time() - t
    t_s[i] = t
# ====================================================================

# # ============================== Delete ==============================
a = list(range(LEN))
shuffle(a)
for i in a:
# ============================== BST =================================
    t = time.process_time()
    del tree[i]
    t = time.process_time() - t
    t_tree[i] = t
# =========================== Hash Table (Chain)======================
    t = time.process_time()
    del c[i]
    t = time.process_time() - t
    t_c[i] = t
# =========================== Hash Table (Chain)======================
    t = time.process_time()
    del p[i]
    t = time.process_time() - t
    t_p[i] = t
# =========================== Skip List ==============================
    t = time.process_time()
    del s[i]
    t = time.process_time() - t
    t_s[i] = t
# ====================================================================


# ===========================plot==============================================

t_tree_10 = list(np.add.reduceat(t_tree, np.arange(0, LEN, 10)))
t_c_10 = list(np.add.reduceat(t_c, np.arange(0, LEN, 10)))
t_p_10 = list(np.add.reduceat(t_p, np.arange(0, LEN, 10)))
t_s_10 = list(np.add.reduceat(t_s, np.arange(0, LEN, 10)))

plt.plot(t_tree_10, 'r', label="BST")
plt.plot(t_c_10, 'b', label = "Hash-chain")
plt.plot(t_p_10, 'g', label = "Hash-probing")
plt.plot(t_s_10, 'm', label = "Skip list")
plt.legend()
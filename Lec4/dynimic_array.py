import ctypes

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""    
    
    def __init__(self):
        """Create an empty array."""
        self._n = 0                                  # count actual elements
        self._capacity = 1                           # default array capacity
        self._A = self._make_array(self._capacity)   #low-level array
    
    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n
    
    def __getitem__(self, k):
        """Return element at index k"""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]                           # retrieve from array
    
    def append(self, obj):
        """Add object to end of the array"""
        if self._n == self._capacity:               # not enough room
            self._resize(2 * self._capacity)        # so double capacity
        self._A[self._n] = obj
        self._n += 1
        
    def _resize(self, c):                           # nonpublic utility
        """Resize internal array to capacity c."""
        B = self._make_array(c)                     # new (bigger) array
        for k in range(self._n):                    # for each existing value
            B[k] = self._A[k]
        self._A = B                                 # use the bigger array
        self._capacity = c
    
    def _make_array(self, c):                       # nonpublic utility
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()    
    
    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward"""
        # (for simplicity, we assume 0 <= k <= n in this version)
        if self._n == self._capacity:           # not enough room
            self._resize(2 * self._capacity)    # so double capacity
        for j in range(self._n, k, -1):         # shift rightmoust first
            self._A[j] = self._A[j-1]
        self._A[k] = value                      # store newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)"""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:             # found a match!
                for j in range(k, self._n - 1): # shift others to fill gap
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None     # help garbage collection
                self._n -= 1                    # we have one less item
                return                          # exit immediately
            raise ValueError('value not found') # only reached if no match
    
"""Proposition 5.1: Let S be a sequence implemented by means of a dynamic array
with initial capacity one, using the strategy of doubling the array size when full.
The total time to perform a series of n append operations in S, starting from S being
empty, is O(n).

Proposition 5.2: Performing a series of n append operations on an initially empty
dynamic array using a fixed increment with each resize takes Ω(n^2) time.
"""


if __name__ == '__main__':
    N = 100
    data0 = [0]*N
    data1 = [0]*N
    data2 = [0]*N
    for n in range(N):
        data0.insert(0, None)
        data1.insert(n // 2, None)
        data2.insert(n, None)
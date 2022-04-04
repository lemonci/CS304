import random
from random import shuffle 
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
    def delete(self, val):
        if self == None:
            return self
        if val < self.pair[0]:
            self.left = self.left.delete(val)
            return self
        if val > self.pair[0]:
            self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node:
            min_larger_node = min_larger_node.left
        self.pair = min_larger_node.pair
        self.right = self.right.delete(min_larger_node.val)
        return self
    def exists(self, val):
        if val == self.pair[0]:
            return True
        if val < self.pair[0]:
            if self.left == None:
                return False
            return self.left.exists(val)
        if self.right == None:
            return False
        return self.right.exists(val)
    def size(self):
        size = 0
        if self != None:
            size += 1
            if self.left != None:
                size += 1 + self.left.size()
            if self.right != None:
                size += 1 + self.right.size()
        return size
    
LEN = 10
keys = list(range(LEN))
shuffle(keys)

    
dic = []
for key in keys:
    dic.append((key, random.random()))